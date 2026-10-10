param([string]$ComsolBin = 'C:\Program Files\COMSOL\COMSOL64\Multiphysics\bin\win64')
$ErrorActionPreference = 'Stop'
$taskRoot = $PSScriptRoot
$buildPath = Join-Path $taskRoot 'build'
New-Item -ItemType Directory -Path $buildPath -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $taskRoot 'verification') -Force | Out-Null
foreach ($caseName in @('A_baseline','B_open_baseline')) {
    $control = Join-Path $taskRoot ('verification\' + $caseName + '_original_baseline.csv')
    Copy-Item -LiteralPath (Join-Path $taskRoot ('data\' + $caseName + '_native.csv')) -Destination $control -Force
}
$source = Get-Content -LiteralPath (Join-Path $taskRoot 'scripts\VerifyMinimal.java') -Raw
$source = $source.Replace('__ROOT__', $taskRoot.Replace('\','/'))
$generated = Join-Path $buildPath 'VerifyMinimal.java'
[System.IO.File]::WriteAllText($generated, $source, [System.Text.UTF8Encoding]::new($false))
Push-Location $buildPath
try {
    & (Join-Path $ComsolBin 'comsolcompile.exe') $generated
    if ($LASTEXITCODE -ne 0) { throw 'COMSOL verification Java compilation failed.' }
    & (Join-Path $ComsolBin 'comsolbatch.exe') -np 2 -inputfile (Join-Path $buildPath 'VerifyMinimal.class') -nosave -batchlog (Join-Path $buildPath 'verify_batch.log')
    if ($LASTEXITCODE -ne 0) { throw 'COMSOL verification execution failed; inspect build/verify_batch.log.' }
}
finally { Pop-Location }
