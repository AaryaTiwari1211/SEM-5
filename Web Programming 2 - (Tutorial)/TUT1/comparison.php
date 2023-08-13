<?php
    $abcd = 57;
    $abce = 11;

    $a = 10;
    $b = "10";

    if ($a == $b) {
        echo "Equal<br><br>";
    } else {
        echo "Not Equal<br><br>";
    }

    $a = 10;
    $b = 20;

    if ($a != $b) {
        echo "Not Equal<br><br>";
    } else {
        echo "Equal<br><br>";
    }

    $a = 10;
    $b = "10";

    if ($a === $b) {
        echo "Identical<br><br>";
    } else {
        echo "Not Identical<br><br>";
    }

    $a = 10;
    $b = 10.0;

    if ($a !== $b) {
        echo "Not Identical<br><br>";
    } else {
        echo "Identical<br><br>";
    }

    $a = 15;
    $b = 10;

    if ($a > $b) {
        echo "Greater than<br><br>";
    } else {
        echo "Not Greater than<br><br>";
    }

    $a = 15;
    $b = 20;

    if ($a < $b) {
        echo "Less than<br><br>";
    } else {
        echo "Not Less than<br><br>";
    }

    $a = 20;
    $b = 20;

    if ($a >= $b) {
        echo "Greater than or equal to<br><br>";
    } else {
        echo "Not Greater than or equal to<br><br>";
    }

    $a = 15;
    $b = 20;

    if ($a <= $b) {
        echo "Less than or equal to<br><br>";
    } else {
        echo "Not Less than or equal to<br><br>";
    }
?>