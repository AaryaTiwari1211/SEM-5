<?php
    session_start();

    // Set session variables
    $_SESSION["user"] = "John";
    $_SESSION["email"] = "john@example.com";

    if (isset($_SESSION["user"])) {
        $user = $_SESSION["user"];
        echo "Welcome, $user!";
    } else {
        echo "Session variable not set.";
    }

    $_SESSION["user"] = "Alice";
    
    session_destroy();
?>