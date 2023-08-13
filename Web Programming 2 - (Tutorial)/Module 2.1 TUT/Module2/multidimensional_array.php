<?php
    $employee = array(
        array(1,"Aarya","12/11/2003"),
        array(2,"Dhairya","31/10/2003"),
        array(3,"Gonka","18/03/2003"),
        array(4,"Dhrumvv","13/07/2003"),
    );
    for($row = 0;$row<4;$row++)
    {
        echo "Details of Employee ".$row+1 ." are as follows:- <br>";
        echo "Id of the employee: " . $employee[$row][0] . "<br>";
        echo "Name of the employee: " . $employee[$row][1] . "<br>";
        echo "Date of Birth of the employee: " . $employee[$row][2] . "<br>";
        echo "<br><br>";
    }
    // Tabular Form
    for($row = 0;$row<4;$row++){
        for($col = 0;$col<3;$col++)
        {
            echo $employee[$row][$col] . " ";
        }
        echo "<br>";
    }
?>