<?php
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
?>