<?php
    $mysqli = new mysqli("localhost", "root", "", "test2");

    if ($mysqli->connect_error) {
        die("Connection failed: " . $mysqli->connect_error);
    }

    if (isset($_POST['add_data'])) {
        $name = $_POST['name'];
        $age = $_POST['age'];
        $email = $_POST['email'];

        $insertSQL = "INSERT INTO student (name, age, email) VALUES ('$name', $age, '$email')";

        if ($mysqli->query($insertSQL) === TRUE) {
            echo "Data added to the database successfully.";
        } else {
            echo "Error adding data: " . $mysqli->error;
        }
    }
?>