<?php
    class Student // Class
    {
        public $name;
        public $age;
        public $gender;
        public $rollno;
        public $marks;
    }
    $a = new Student(); // Object
    $a->name = "Aarya";
    $a->age = 11;
    $a->gender = "Male";
    $a->rollno = 1;
    $a->marks = 100;

    if ($a instanceof Student) { // Instanceof
        echo "$a->name is a Student.";
    } 
    else {
        echo "Not a Student.";
    }
?>