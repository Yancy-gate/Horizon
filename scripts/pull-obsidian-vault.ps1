# Pull Obsidian vault + ensure today's Beijing-dated briefing exists.
# Bypasses HTTP proxy. Scheduled daily at 07:00 / 07:30.

$ErrorActionPreference = "Continue"
$LogDir = Join-Path $env:USERPROFILE "Projects\Horizon\scripts\logs"
$LogFile = Join-Path $LogDir ("obsidian-pull-{0}.log" -f (Get-Date -Format "yyyy-MM-dd"))
$HorizonRoot = Join-Path $env:USERPROFILE "Projects\Horizon"
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
    $obsidianRoot = "D:\Tools\editor\Obsidian"
    $vault = Get-ChildItem -LiteralPath $obsidianRoot -Directory -ErrorAction Stop |
        Where-Object {
            (Test-Path -LiteralPath (Join-Path $_.FullName ".git")) -and
            ((git -C $_.FullName remote get-url origin 2>$null) -match "obsidian_cloud")
        } |
        Select-Object -First 1
    if (-not $vault) { throw "No obsidian_cloud vault under $obsidianRoot" }
    $VaultRoot = $vault.FullName
    Write-Log "Vault: $VaultRoot"

    $r = Invoke-GitNoProxy $VaultRoot @("pull", "--ff-only", "origin", "master")
    Write-Log ("Vault pull: " + $r.Out)
    if ($r.Code -ne 0) { throw "vault git pull failed: $($r.Code)" }

    # Also refresh Horizon repo and copy latest ZH briefing if needed
    if (Test-Path -LiteralPath $HorizonRoot) {
        $h = Invoke-GitNoProxy $HorizonRoot @("pull", "--ff-only", "origin", "main")
        Write-Log ("Horizon pull: " + $h.Out)

        $bj = Get-Date -Format "yyyy-MM-dd"
        $briefDir = Get-ChildItem -LiteralPath $VaultRoot -Recurse -Directory -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -eq "内参日报" } |
            Select-Object -First 1 -ExpandProperty FullName
        if (-not $briefDir) {
            $briefDir = Join-Path $VaultRoot "其他\内参日报"
            New-Item -ItemType Directory -Force -Path $briefDir | Out-Null
        }

        $target = Join-Path $briefDir "horizon-$bj-zh.md"
        $srcDir = Join-Path $HorizonRoot "data\summaries"
        $latest = Get-ChildItem -LiteralPath $srcDir -Filter "horizon-*-zh.md" -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if ($latest) {
            if (-not (Test-Path -LiteralPath $target)) {
                Copy-Item -LiteralPath $latest.FullName -Destination $target -Force
                Write-Log "Copied $($latest.Name) -> horizon-$bj-zh.md"
            } else {
                Write-Log "Briefing already present: horizon-$bj-zh.md"
            }
        } else {
            Write-Log "No ZH summary in Horizon data/summaries yet."
        }
    }

    exit 0
} catch {
    Write-Log ("ERROR: " + $_.Exception.Message)
    exit 1
}
