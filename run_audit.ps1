# Context Entropy Auditor (CEA) - PowerShell Runner
[CmdletBinding()]
param (
    [string]$File = "",
    [string]$Model = "gemini-3.7-flash",
    [string]$Effort = "medium",
    [switch]$Interactive
)

$ErrorActionPreference = "Stop"

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  CONTEXT ENTROPY AUDITOR (CEA) - Windows PowerShell Launcher" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

$ProjectRoot = $PSScriptRoot
$env:PYTHONPATH = Join-Path $ProjectRoot "src"

$agyCmd = Get-Command "agy.exe" -ErrorAction SilentlyContinue
if ($agyCmd) {
    Write-Host "  [OK] Antigravity CLI detectado: $($agyCmd.Source)" -ForegroundColor Green
} else {
    Write-Host "  [AVISO] agy.exe no encontrado en PATH. Se usara adaptador remoto si aplica." -ForegroundColor Yellow
}

if ($Interactive -or [string]::IsNullOrWhiteSpace($File)) {
    Write-Host "  Iniciando CLI Interactivo y Live Stress Test Suite..." -ForegroundColor Green
    python -m context_auditor.cli --interactive --model $Model --effort $Effort
} else {
    Write-Host "  Auditando archivo: $File (Modelo: $Model, Effort: $Effort)..." -ForegroundColor Green
    python -m context_auditor.cli $File --adapter antigravity --model $Model --effort $Effort
}
