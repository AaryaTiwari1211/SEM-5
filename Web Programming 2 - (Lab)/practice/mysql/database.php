<?php
    $mysqli = new mysqli("localhost", "root", "", "test2");
    if ($mysqli->connect_error) {
        die("Connection failed: " . $mysqli->connect_error);
    } else {
        echo "Connected successfully!";
    }
?>