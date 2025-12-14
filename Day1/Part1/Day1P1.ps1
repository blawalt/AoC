$lines = Get-Content -Path input.txt
$StartingPt = 50
$pass = 0

foreach ($line in $lines){
    $direction = $line.Substring(0,1)
    $mvmt = [int]($line.Substring(1))
    if ($direction -eq "R"){$StartingPt += $mvmt}
    else {$StartingPt -= $mvmt}
    $StartingPt = (100 + $StartingPt % 100) % 100
    if ($StartingPt -eq 0){$pass++}
}
