param(
  [string]$BaseUrl = "http://localhost:8000",
  [int]$Users = 25,
  [int]$RampUp = 30,
  [int]$Duration = 120,
  [string]$Scenario = "docker-compose",
  [int]$Nodes = 1,
  [int]$Replicas = 1
)

$ErrorActionPreference = "Stop"
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$outDir = Join-Path $PSScriptRoot "..\results\$Scenario-n$Nodes-r$Replicas-u$Users-$timestamp"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

jmeter -n `
  -t (Join-Path $PSScriptRoot "..\jmeter\covagro-load-test.jmx") `
  -l (Join-Path $outDir "samples.jtl") `
  -e -o (Join-Path $outDir "dashboard") `
  -JBASE_URL=$BaseUrl `
  -JUSERS=$Users `
  -JRAMP_UP=$RampUp `
  -JDURATION=$Duration

Write-Host "Resultados en $outDir"
