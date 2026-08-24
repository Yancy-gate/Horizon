param(
    [string]$VaultRoot = "D:\Data\旧的不去新的不来",
    [string]$Remote = "origin",
    [string]$Branch = "master"
)

# Pull the Git-backed Obsidian vault. Intended for Windows Task Scheduler.
$ErrorActionPreference = "Stop"
$LogDir = Join-Path $PSScriptRoot "logs"
$LogFile = Join-Path $LogDir ("obsidian-pull-{0}.log" -f (Get-Date -Format "yyyy-MM-dd"))
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

function Write-Log([string]$msg) {
    $line = "{0} {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $msg
    Add-Content -LiteralPath $LogFile -Value $line -Encoding UTF8
    Write-Host $line
}

function Invoke-GitNoProxy {
    param([string]$WorkDir, [string[]]$GitArgs)
    $prev = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"
    $out = & git -c http.proxy= -c https.proxy= -C $WorkDir @GitArgs 2>&1 | Out-String
    $code = $LASTEXITCODE
    $ErrorActionPreference = $prev
    return @{ Code = $code; Out = $out.Trim() }
}

try {
    if (-not (Test-Path -LiteralPath (Join-Path $VaultRoot ".git"))) {
        throw "Obsidian vault is not a Git repository: $VaultRoot"
    }

    $remoteUrl = Invoke-GitNoProxy $VaultRoot @("remote", "get-url", $Remote)
    if ($remoteUrl.Code -ne 0) {
        throw "Git remote '$Remote' is not configured in $VaultRoot"
    }
    if ($remoteUrl.Out -notmatch "obsidian-jiudebuqu-xindebulai") {
        throw "Unexpected Obsidian remote: $($remoteUrl.Out)"
    }

    Write-Log "Vault: $VaultRoot"
    Write-Log "Remote: $($remoteUrl.Out)"

    $r = Invoke-GitNoProxy $VaultRoot @("pull", "--ff-only", $Remote, $Branch)
    Write-Log ("Vault pull: " + $r.Out)
    if ($r.Code -ne 0) { throw "vault git pull failed: $($r.Code)" }

    $today = Get-Date -Format "yyyy-MM-dd"
    $briefing = Join-Path $VaultRoot "其他\内参日报\horizon-$today-zh.md"
    if (Test-Path -LiteralPath $briefing) {
        Write-Log "Today's briefing is present: horizon-$today-zh.md ($((Get-Item -LiteralPath $briefing).Length) bytes)"
    } else {
        Write-Log "Today's briefing is not on the remote yet; the next scheduled pull will retry."
    }

    exit 0
} catch {
    Write-Log ("ERROR: " + $_.Exception.Message)
    exit 1
}
