<?php
    echo "Hello World! <br>"; 
    $a = 11;
    $b = 57;
    echo "Number 1 is " . $a . "<br>";
    echo "Number 2 is " . $b . "<br><br>";
    
    $k = $a += $b;
    echo $k . " -- Addition Assignment <br><br>"; // Addition Assignment

    $l = $a -= $b;
    echo $l . " -- Subtraction Assignment <br><br>"; // Subtraction Assignment

    $n = $a *= $b;
    echo $n . " -- Multiplication Assignment <br><br>"; // Multiplication Assignment

    $o = $a /= $b;
    echo $o . " -- Division Assignment <br><br>"; // Division Assignment

    $p = $a %= $b;
    echo $p . " --  Modulus Assignment <br><br>"; // Modulus Assignment

    $q = $a **= $b;
    echo $q . " -- Exponentiation Assignment <br><br>"; // Exponentiation Assignment
?>