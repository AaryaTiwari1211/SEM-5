<?php
    $a = array(11, 12, 13, 14, 15, 16, 17, 18, 19, 20); // Array
    echo $a[0] . "<br><br>"; // Array Index
    echo $a[1] . "<br><br>"; // Array Index

    $b = array("Aarya", "Aaryan", "Aarav", "Aarush", "Aarohi"); // Array
    echo $b[0] . "<br><br>"; // Array Index
    echo $b[1] . "<br><br>"; // Array Index

    $c = array("Aarya" => 11, "Aaryan" => 12, "Aarav" => 13, "Aarush" => 14, "Aarohi" => 15); // Associative Array
    $d = array("Aarya" => 11, "Aaryan" => 12, "Aarav" => 13, "Aarush" => 14, "Aarohi" => 15); // Associative Array

    print_r($c + $d); // Union
    // $c + $d . "<br><br>"; // Union

    $a = [1, 2, 3];
    $b = [1, 2, 4];

    if ($a != $b) {
        echo "<br>Arrays are not equal.<br><br>";
    } else {
        echo "<br>Both arrays are equal.<br><br>";
    }

    $a = [1, 2, 'three'];
    $b = [1, 2, '3'];

    if ($a === $b) {
        echo "Both arrays are identical.<br><br>";
    } else {
        echo "Arrays are not identical.<br><br>";
    }
    
    $a = [1, 2, 3];
    $b = [1, 2, 3];

    if ($a !== $b) {
        echo "Arrays are not identical.<br><br>";
    } else {
        echo "Both arrays are identical.<br><br>";
    }

    $a = [1, 2, 3];
    $b = [1, 2, 4];

    if ($a <> $b) {
        echo "Arrays are not equal.<br><br>";
    } else {
        echo "Both arrays are equal.<br><br>";
    }
?>