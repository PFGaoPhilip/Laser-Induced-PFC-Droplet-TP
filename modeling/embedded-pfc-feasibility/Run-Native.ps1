param([string]$ComsolBin='C:\Program Files\COMSOL\COMSOL64\Multiphysics\bin\win64')
$ErrorActionPreference='Stop'
$taskRoot=$PSScriptRoot
$buildPath=Join-Path $taskRoot 'build'
New-Item -ItemType Directory -Path $buildPath -Force | Out-Null
foreach ($name in @('EmbeddedPfc.java','NativePfcEOS.java','NativeCases.java')) {
  $source=Get-Content -LiteralPath (Join-Path $taskRoot ('scripts\'+$name)) -Raw
  $source=$source.Replace('__ROOT__',$taskRoot.Replace('\','/'))
  [System.IO.File]::WriteAllText((Join-Path $buildPath $name),$source,[System.Text.UTF8Encoding]::new($false))
}
Push-Location $buildPath
try {
  foreach ($name in @('NativePfcEOS','NativeCases','EmbeddedPfc')) {
    $compileStart=Get-Date
    & (Join-Path $ComsolBin 'comsolcompile.exe') ($name+'.java')
    $classPath=Join-Path $buildPath ($name+'.class')
    if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $classPath) -or
        (Get-Item -LiteralPath $classPath).LastWriteTime -lt $compileStart) {
      throw ('COMSOL compilation failed: '+$name)
    }
  }
  & (Join-Path $ComsolBin 'comsolbatch.exe') -np 2 -inputfile EmbeddedPfc.class -nosave -batchlog (Join-Path $buildPath 'native_batch.log')
  if ($LASTEXITCODE -ne 0) {throw 'COMSOL run failed; inspect build/native_batch.log'}
}
finally {Pop-Location}
