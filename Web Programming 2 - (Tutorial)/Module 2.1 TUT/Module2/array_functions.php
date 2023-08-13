<?php  
    function printArray($arr)
    {
        echo "<br>";
        foreach($arr as $a)
        {
            echo "$a <br>";
        }
    }
    $b2 = array("Aarya","Dev","Smit","Mihir","Siddarth","Riya","Hussain","Advait","Parth","Sumit","Om","Tanmay","Prathamesh","Arpan","Twisha");
    $b2frands = array("Aarya","Dhairya","Smit","Gonka","Dhrumvv");  

    echo "The people in B2 are: ";
    printArray($b2);

    //Changing Key Cases
    // echo "After changing the key cases";
    // $b2case = array_change_key_case($b2,CASE_UPPER);
    // printArray($b2case);
    // echo "<br><br>";   

    //Array Chunk Function
    print_r(array_chunk($b2,3));
    echo "<br><br>";  

    //Count Function
    echo "The Number of elements in the Array is: " . count($b2) . "<br>";
    echo "<br><br>";

    //Sort Function
    sort($b2);
    echo "The Sorted Array is: ";
    printArray($b2);
    // print_r($b2);
    echo "<br><br>";

    //Reversing the Array
    $reverseArray = array_reverse($b2);
    echo "The Reversed Array is: ";
    printArray($reverseArray);
    // print_r($reverseArray);
    echo "<br><br>";

    //Searching in An Array
    $key = array_search("Dev",$b2);
    // $key+=1;
    gettype($key);
    if($key == false)
    {
        echo "Dev was not found in the Array <br><br>";
    }
    else
    {
        echo "Dev is at position $key in the Array";
        echo "<br><br>";
    }

    //Intersection of an Array
    $prevb2 = array_intersect($b2,$b2frands);
    echo "The previous members in the B2 Batch are: ";
    print_r($prevb2);

       
?>    