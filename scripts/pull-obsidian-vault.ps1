# Pull Obsidian vault + ensure today's Beijing-dated briefing exists.
# Run after Daily Horizon Summary (12:00 CST generation → pull ~12:30).

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

function Resolve-VaultRoot {
    param([string]$PreferredPath)

    if ($PreferredPath -and (Test-Path -LiteralPath (Join-Path $PreferredPath ".git"))) {
        return $PreferredPath
    }

    $searchRoots = @(
        "D:\Data\旧的不去新的不来",
        "D:\Tools\editor\Obsidian"
    )

    foreach ($root in $searchRoots) {
        if (-not (Test-Path -LiteralPath $root)) { continue }

        if ((Test-Path -LiteralPath (Join-Path $root ".git"))) {
            $remote = git -C $root remote get-url origin 2>$null
            if ($remote -match "obsidian-jiudebuqu-xindebulai|obsidian_cloud") {
                return $root
            }
        }

        $vault = Get-ChildItem -LiteralPath $root -Directory -ErrorAction SilentlyContinue |
            Where-Object {
                (Test-Path -LiteralPath (Join-Path $_.FullName ".git")) -and
                ((git -C $_.FullName remote get-url origin 2>$null) -match "obsidian-jiudebuqu-xindebulai|obsidian_cloud")
            } |
            Select-Object -First 1
        if ($vault) { return $vault.FullName }
    }

    return $null
}

try {
    $preferredVault = $env:HORIZON_OBSIDIAN_VAULT
    $VaultRoot = Resolve-VaultRoot -PreferredPath $preferredVault
    if (-not $VaultRoot) {
        throw "No Obsidian vault found (set HORIZON_OBSIDIAN_VAULT or clone obsidian-jiudebuqu-xindebulai)"
    }
    Write-Log "Vault: $VaultRoot"

    $r = Invoke-GitNoProxy $VaultRoot @("pull", "--rebase", "--autostash", "origin", "master")
    Write-Log ("Vault pull: " + $r.Out)
    if ($r.Code -ne 0) { throw "vault git pull failed: $($r.Code)" }

    if (Test-Path -LiteralPath $HorizonRoot) {
        $h = Invoke-GitNoProxy $HorizonRoot @("pull", "--ff-only", "origin", "main")
        Write-Log ("Horizon pull: " + $h.Out)
    }

    $bj = Get-Date -Format "yyyy-MM-dd"
    $briefDir = Join-Path $VaultRoot "其他\内参日报"
    if (-not (Test-Path -LiteralPath $briefDir)) {
        $sample = Get-ChildItem -LiteralPath $VaultRoot -Recurse -Filter "horizon-*-zh.md" -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1
        if (-not $sample) { throw "No horizon-*-zh.md found in vault; wait for Actions sync." }
        $briefDir = $sample.DirectoryName
    }
    Write-Log "Briefing dir: $briefDir"

    $target = Join-Path $briefDir "horizon-$bj-zh.md"
    if (Test-Path -LiteralPath $target) {
        Write-Log "Briefing already present: horizon-$bj-zh.md ($((Get-Item -LiteralPath $target).Length) bytes)"
    } else {
        $candidates = @()
        $candidates += Get-ChildItem -LiteralPath $briefDir -Filter "horizon-*-zh.md" -ErrorAction SilentlyContinue
        $srcDir = Join-Path $HorizonRoot "data\summaries"
        if (Test-Path -LiteralPath $srcDir) {
            $candidates += Get-ChildItem -LiteralPath $srcDir -Filter "horizon-*-zh.md" -ErrorAction SilentlyContinue
        }

        $ranked = foreach ($c in $candidates) {
            if ($c.Name -match 'horizon-(\d{4}-\d{2}-\d{2})-zh\.md') {
                [PSCustomObject]@{
                    File = $c
                    Date = [datetime]::ParseExact($Matches[1], 'yyyy-MM-dd', $null)
                }
            }
        }
        $latest = $ranked | Sort-Object Date -Descending | Select-Object -First 1
        if ($latest) {
            Copy-Item -LiteralPath $latest.File.FullName -Destination $target -Force
            Write-Log ("Copied {0} ({1} bytes) -> horizon-{2}-zh.md" -f $latest.File.Name, $latest.File.Length, $bj)

            $rel = $target.Substring($VaultRoot.Length).TrimStart('\', '/').Replace('\', '/')
            $add = Invoke-GitNoProxy $VaultRoot @("add", "--", $rel)
            $diff = Invoke-GitNoProxy $VaultRoot @("diff", "--cached", "--quiet")
            if ($diff.Code -ne 0) {
                $null = Invoke-GitNoProxy $VaultRoot @("commit", "-m", "🌅 Horizon daily briefing $bj (calendar align)")
                $push = Invoke-GitNoProxy $VaultRoot @("push", "origin", "master")
                Write-Log ("Vault push: " + $push.Out)
            } else {
                Write-Log "Vault already has calendar-aligned briefing committed."
            }
        } else {
            Write-Log "No ZH summary available to copy for $bj."
        }
    }

    exit 0
} catch {
    Write-Log ("ERROR: " + $_.Exception.Message)
    exit 1
}
