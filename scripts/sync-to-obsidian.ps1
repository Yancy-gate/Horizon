# Sync Horizon daily summaries into the Obsidian vault.
# Run manually or via Windows Task Scheduler after GitHub Actions completes.

$ErrorActionPreference = "Stop"

$HorizonRoot = "C:\Users\hproy\Projects\Horizon"
$VaultRoot = "D:\Tools\editor\Obsidian\临时"
$TargetDir = Join-Path $VaultRoot "其他\内参日报"
$Today = Get-Date -Format "yyyy-MM-dd"

Set-Location $HorizonRoot
git pull --ff-only origin main

$SummaryZh = Join-Path $HorizonRoot "data\summaries\horizon-$Today-zh.md"
$SummaryEn = Join-Path $HorizonRoot "data\summaries\horizon-$Today-en.md"

New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null

$copied = $false
foreach ($file in @($SummaryZh, $SummaryEn)) {
    if (Test-Path $file) {
        Copy-Item $file $TargetDir -Force
        Write-Host "Copied $(Split-Path $file -Leaf)"
        $copied = $true
    }
}

if (-not $copied) {
    Write-Host "No summaries found for $Today in $HorizonRoot\data\summaries"
    exit 0
}

Set-Location $VaultRoot
git add "其他/内参日报"
if (git diff --cached --quiet) {
    Write-Host "Obsidian vault already contains today's summaries."
    exit 0
}

git commit -m "🌅 Horizon daily briefing $Today"
git push origin master
Write-Host "Pushed summaries to obsidian_cloud."
