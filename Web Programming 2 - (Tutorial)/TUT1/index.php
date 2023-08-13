<?php
    echo "Hello World! <br>"; 
    $a = 11;
    $b = 57;
    echo "Number 1 is " . $a . "<br>";
    echo "Number 2 is " . $b . "<br><br>";

    $c = $a + $b;
    echo $c . " -- Addition <br><br>"; // Addition

    $d = $a - $b;
    echo $d . " -- Subtraction <br><br>"; // Subtraction

    $e = $a * $b;
    echo $e . " -- Multiplication <br><br>"; // Multiplication

    $f = $a / $b;
    echo $f . " -- Division <br><br>"; // Division

    $g = $a % $b;
    echo $g . " -- Modulus <br><br>"; // Modulus

    $h = $a ** $b;
    echo $h . " -- Exponentiation <br><br>"; // Exponentiation

    $i = $a++;
    echo $i . " -- Increment Addition <br><br>"; // Increment

    $j = $a--;
    echo $j . " -- Decrement Addition <br><br>"; // Decrement

    $k = $a += $b;
    echo $k . " -- Addition Assignment <br><br>"; // Addition Assignment

    $l = $a -= $b;
    echo $l . " -- Subtraction Assignment <br><br>"; // Subtraction Assignment

    $m = $b; 
    echo $m . " -- Assignment <br><br>"; // Assignment

    $n = $a *= $b;
    echo $n . " -- Multiplication Assignment <br><br>"; // Multiplication Assignment

    $o = $a /= $b;
    echo $o . " -- Division Assignment <br><br>"; // Division Assignment

    $p = $a %= $b;
    echo $p . " --  Modulus Assignment <br><br>"; // Modulus Assignment

    $q = $a **= $b;
    echo $q . " -- Exponentiation Assignment <br><br>"; // Exponentiation Assignment


    $abcd = 57;
    $abce = 11;

    $hello = $abcd & $abce;
    echo $hello . " -- And <br><br>"; // And

    $ae = $abcd | $abce;
    echo $ae . " -- Or <br><br>"; // Or

    $af = $abcd ^ $abce;
    echo $af . " -- Xor <br><br>"; // Xor

    $ag = ~$abcd;
    echo $ag . " -- Not <br><br>"; // Not

    $ah = $abcd << $abce;
    echo $ah . " -- Shift Left <br><br>"; // Shift Left

    $ai = $abcd >> $abce;
    echo $ai . " -- Shift Right <br><br>"; // Shift Right

    $s = $abcd == $abce;
    echo $s . " -- Equality <br><br>"; // Equalabcd

    $t = $abcd === $abce;
    echo $t . " -- Identical <br><br>"; // Identical

    $u = $abcd != $abce;
    echo $u . " --  Not Equal <br><br>"; // Not Equal

    $w = $abcd !== $abce;
    echo $w . " -- Not Identical <br><br>"; // Not Identical

    $x = $abcd < $abce;
    echo $x . " -- Addition <br><br>"; // Less Than

    $y = $abcd > $abce;
    echo $y . " -- Greater Than <br><br>"; // Greater Than

    $z = $abcd <= $abce;
    echo $z . " -- Less Than or Equal To <br><br>"; // Less Than or Equal To

    $aa = $abcd >= $abce;
    echo $aa . " -- Greater Than or Equal To <br><br>"; // Greater Than or Equal To

    $ab = $abcd <=> $abce;
    echo $ab . " -- Spaceship Addition <br><br>"; // Spaceship 

    $ak = $abcd || $abce;
    echo $ak . " -- Or <br><br>"; // Or

    $al = $abcd ?? $abce;
    echo $al . " -- Null Coalescing Operator <br><br>"; // Null Coalescing Operator

    $am = $abcd . $abce;
    echo $am . " -- Concatenation <br><br>"; // Concatenation

    $an = $abcd .= $abce;
    echo $an . " -- Concatenation Assignment <br><br>"; // Concatenation Assignment

?>