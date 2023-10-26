<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $age = $_POST["age"];
    $phone = $_POST["phone"];
    $address = $_POST["address"];

    $errors = [];

    if (empty($name) || empty($email) || empty($age) || empty($phone) || empty($address)) {
        $errors[] = "Please fill all the fields";
    }

    if (!preg_match("/^[0-9]{10}$/", $phone)) {
        $errors[] = "Phone number is invalid";
    }

    if ($email != filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Email is invalid";
    }
}

if (empty($errors)) {
    // Data is valid, you can process it here
    echo "Form submitted successfully! Data received:<br>";
    echo "Name: $name<br>";
    echo "Phone: $phone<br>";
    echo "Age: $age<br>";
    echo "Address: $address<br>";
    echo "Email: $email<br>";
} else {
    // Display validation errors
    echo "Validation errors:<br>";
    foreach ($errors as $error) {
        echo "- $error<br>";
    }
}

?>