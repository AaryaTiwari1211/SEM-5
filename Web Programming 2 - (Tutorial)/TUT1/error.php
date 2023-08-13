<?php
    function divideNumbers($numerator, $denominator)
    {
        return $numerator / $denominator;
    }
    $result = @divideNumbers(10, 0);

    if ($result === false) {
        echo "An error occurred during division.";
    } else {
        echo "Result: $result";
}
?>