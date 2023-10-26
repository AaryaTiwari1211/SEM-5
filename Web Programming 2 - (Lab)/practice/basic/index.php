<?php

    // PHP Syntax
    echo "Hello, World!";

    // Variables
    $name = "John";
    $age = 30;

    //Data Types
    $integer = 42;
    $float = 3.14;
    $string = "Hello, PHP!";
    $boolean = true;
    $array = array(1, 2, 3);

    // Operators and Arithematic
    $x = 10;
    $y = 3;
    $sum = $x + $y;
    $difference = $x - $y;
    $product = $x * $y;
    $quotient = $x / $y;

    // Defining Constants
    define("PI", 3.14);
    echo PI; 

    // If-Else Statements
    $age = 18;
    if ($age < 18) {
        echo "You are a minor.";
    } elseif ($age >= 18 && $age < 65) {
        echo "You are an adult.";
    } else {
        echo "You are a senior citizen.";
    }

    // Switch Case Statements

    $day = "Monday";
    switch ($day) {
        case "Monday":
            echo "It's the start of the workweek.";
            break;
        case "Friday":
            echo "It's almost the weekend.";
            break;
        default:
            echo "It's another day.";
    }

    // Loops
    for ($i = 1; $i <= 5; $i++) {
        echo "Iteration $i<br>";
    }
    
    $fruits = array("Apple", "Banana", "Cherry");
    foreach ($fruits as $fruit) {
        echo $fruit . "<br>";
    }
    
    $num = 0;
    while ($num < 5) {
        echo "Number: $num<br>";
        $num++;
    }

    // User defined Functions
    function greet($name) {
        echo "Hello, $name!";
    }
    
    greet("Alice"); 
    
    function add($x, $y) {
        return $x + $y;
    }
    
    $result = add(10, 20); 


    // Arrays
    $fruits = array("Apple", "Banana", "Cherry");
    echo $fruits[0]; 

    $person = array("name" => "John", "age" => 30);
    echo $person["name"];
?>