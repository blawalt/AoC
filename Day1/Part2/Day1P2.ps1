Measure-Command{$startingPt = 50
$key_to_door = 0
$input = Get-Content -Path "input.txt"

foreach($line in $input){
    $direction = $line.Substring(0,1)
    $mvmt = [int]$line.Substring(1)
    if ($direction -eq "L"){$multiplier = -1} else {$multiplier = 1}
    $target = $startingPt + ($mvmt * $multiplier)
    $crossings = [Math]::Abs([Math]::Floor($target / 100) - [Math]::Floor($startingPt / 100))
    $key_to_door += $crossings
    $startingPt = $target
}
}