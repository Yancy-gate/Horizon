param(
    [string]$VaultRoot = "D:\Data\旧的不去新的不来",
    [string]$DailyAt = "07:30",
    [string]$TaskName = "Horizon Obsidian Daily Pull"
)

$ErrorActionPreference = "Stop"
$pullScript = Join-Path $PSScriptRoot "pull-obsidian-vault.ps1"

if (-not (Test-Path -LiteralPath $pullScript)) {
    throw "Pull script not found: $pullScript"
}
if (-not (Test-Path -LiteralPath (Join-Path $VaultRoot ".git"))) {
    throw "Obsidian vault is not a Git repository: $VaultRoot"
}

try {
    $scheduleTime = [datetime]::ParseExact(
        $DailyAt,
        "HH:mm",
        [Globalization.CultureInfo]::InvariantCulture
    )
} catch {
    throw "DailyAt must use 24-hour HH:mm format, for example 07:30."
}

$powerShellExe = (Get-Process -Id $PID).Path
$arguments = @(
    "-NoProfile"
    "-NonInteractive"
    "-ExecutionPolicy", "Bypass"
    "-File", "`"$pullScript`""
    "-VaultRoot", "`"$VaultRoot`""
) -join " "

Write-Host "Testing the pull command before installing the task..."
& $powerShellExe `
    -NoProfile `
    -NonInteractive `
    -ExecutionPolicy Bypass `
    -File $pullScript `
    -VaultRoot $VaultRoot
if ($LASTEXITCODE -ne 0) {
    throw "The pull test failed with exit code $LASTEXITCODE. The task was not installed."
}

$action = New-ScheduledTaskAction `
    -Execute $powerShellExe `
    -Argument $arguments `
    -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -Daily -At $scheduleTime
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15)
$principal = New-ScheduledTaskPrincipal `
    -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) `
    -LogonType Interactive `
    -RunLevel Limited

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "Pull Horizon daily briefings into the active Obsidian vault." `
    -Force | Out-Null

$task = Get-ScheduledTask -TaskName $TaskName
Write-Host "Installed task: $($task.TaskName)"
Write-Host "Daily schedule: $DailyAt"
Write-Host "Vault: $VaultRoot"
