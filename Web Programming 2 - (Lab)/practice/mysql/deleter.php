<?php
    $mysqli = new mysqli("localhost", "root", "", "test2");

    if ($mysqli->connect_error) {
        die("Connection failed: " . $mysqli->connect_error);
    }

    if (isset($_POST['delete_data'])) {
        $id = $_POST['id'];

        $deleteSQL = "DELETE FROM student WHERE id = $id";

        if ($mysqli->query($deleteSQL) === TRUE) {
            echo "Data deleted successfully.";
        } else {
            echo "Error deleting data: " . $mysqli->error;
        }
    }
?>