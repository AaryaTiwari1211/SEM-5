<?php
$mysqli = new mysqli("localhost", "root", "", "test2");

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

if (isset($_POST['update_data'])) {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $age = $_POST['age'];
    $email = $_POST['email'];

    $updateSQL = "UPDATE student SET name = '$name', age = $age, email = '$email' WHERE id = $id";

    if ($mysqli->query($updateSQL) === TRUE) {
        echo "Data updated successfully.";
    } else {
        echo "Error updating data: " . $mysqli->error;
    }
}
?>