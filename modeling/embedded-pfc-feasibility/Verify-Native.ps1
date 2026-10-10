param([string]$ComsolBin='C:\Program Files\COMSOL\COMSOL64\Multiphysics\bin\win64')
$ErrorActionPreference='Stop'
$taskRoot=$PSScriptRoot
$buildPath=Join-Path $taskRoot 'build'
New-Item -ItemType Directory -Path $buildPath -Force | Out-Null
$source=Get-Content -LiteralPath (Join-Path $taskRoot 'scripts\VerifyEmbedded.java') -Raw
$source=$source.Replace('__ROOT__',$taskRoot.Replace('\','/'))
[System.IO.File]::WriteAllText((Join-Path $buildPath 'VerifyEmbedded.java'),$source,[System.Text.UTF8Encoding]::new($false))
Push-Location $buildPath
try {
  $compileStart=Get-Date
  & (Join-Path $ComsolBin 'comsolcompile.exe') VerifyEmbedded.java
  $classPath=Join-Path $buildPath 'VerifyEmbedded.class'
  if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $classPath) -or
      (Get-Item -LiteralPath $classPath).LastWriteTime -lt $compileStart) {throw 'Native verifier compilation failed'}
  & (Join-Path $ComsolBin 'comsolbatch.exe') -np 2 -inputfile VerifyEmbedded.class -nosave -batchlog (Join-Path $taskRoot 'verification\native_reload.log')
  if ($LASTEXITCODE -ne 0) {throw 'Native verifier run failed; inspect verification/native_reload.log'}
}
finally {Pop-Location}
