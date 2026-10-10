param([string]$ComsolBin = 'C:\Program Files\COMSOL\COMSOL64\Multiphysics\bin\win64')
$ErrorActionPreference = 'Stop'
$taskRoot = $PSScriptRoot
$buildPath = Join-Path $taskRoot 'build'
$verificationPath = Join-Path $taskRoot 'verification'
New-Item -ItemType Directory -Path $buildPath -Force | Out-Null
New-Item -ItemType Directory -Path $verificationPath -Force | Out-Null
$source = Get-Content -LiteralPath (Join-Path $taskRoot 'scripts\VerifyGuideInputs.java') -Raw
$source = $source.Replace('__ROOT__', $taskRoot.Replace('\','/'))
$generated = Join-Path $buildPath 'VerifyGuideInputs.java'
[System.IO.File]::WriteAllText($generated, $source, [System.Text.UTF8Encoding]::new($false))
$batchLog = Join-Path $buildPath 'guide_import_check.log'
$record = Join-Path $verificationPath 'GUIDE_NATIVE_IMPORT_CHECK.txt'
Push-Location $buildPath
try {
    & (Join-Path $ComsolBin 'comsolcompile.exe') $generated
    if ($LASTEXITCODE -ne 0) { throw 'Guide-check Java compilation failed.' }
    $nativeOutput = & (Join-Path $ComsolBin 'comsolbatch.exe') -np 2 -inputfile (Join-Path $buildPath 'VerifyGuideInputs.class') -nosave -batchlog $batchLog
    $nativeExit = $LASTEXITCODE
    $nativeOutput | Set-Content -LiteralPath $record -Encoding UTF8
    $text = $nativeOutput -join "`n"
    if ($nativeExit -ne 0 -or (Get-Content -LiteralPath $batchLog -Raw) -match 'Error running java class\.') {
        throw 'Guide-check native execution failed; inspect build/guide_import_check.log.'
    }
    if ($text -notmatch 'GUIDE_NATIVE_IMPORT_CONVERSION_COMPLETE') {
        throw 'Guide-check completion marker missing; inspect the native output and batch log.'
    }
    Write-Output $text
}
finally { Pop-Location }
