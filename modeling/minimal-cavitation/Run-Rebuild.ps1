param(
    [string]$ComsolBin = 'C:\Program Files\COMSOL\COMSOL64\Multiphysics\bin\win64'
)
$ErrorActionPreference = 'Stop'
$taskRoot = $PSScriptRoot
$buildPath = Join-Path $taskRoot 'build'
New-Item -ItemType Directory -Path $buildPath -Force | Out-Null
foreach ($subfolder in @('models','data','verification')) {
    New-Item -ItemType Directory -Path (Join-Path $taskRoot $subfolder) -Force | Out-Null
}
$source = Get-Content -LiteralPath (Join-Path $taskRoot 'scripts\MinimalCavitation.java') -Raw
$source = $source.Replace('__ROOT__', $taskRoot.Replace('\','/'))
$generatedSource = Join-Path $buildPath 'MinimalCavitation.java'
[System.IO.File]::WriteAllText($generatedSource, $source, [System.Text.UTF8Encoding]::new($false))
Push-Location $buildPath
try {
    & (Join-Path $ComsolBin 'comsolcompile.exe') $generatedSource
    if ($LASTEXITCODE -ne 0) { throw 'COMSOL Java compilation failed.' }
    & (Join-Path $ComsolBin 'comsolbatch.exe') -np 2 -inputfile (Join-Path $buildPath 'MinimalCavitation.class') -nosave -batchlog (Join-Path $buildPath 'native_batch.log')
    if ($LASTEXITCODE -ne 0) { throw 'COMSOL batch execution failed; inspect build/native_batch.log.' }
}
finally { Pop-Location }
