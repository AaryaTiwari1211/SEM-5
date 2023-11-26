<?php
    function square(&$num)
    {
        $num = $num * $num;
    }

    $value = 5;
    echo "Before: $value\n"; // Before: 5

    square($value);
    echo "After: $value\n"; // After: 25
?>