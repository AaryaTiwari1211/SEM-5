<?php
    $cookie_name = "user";
    $cookie_value = "John";
    $expiration = time() + 3600;

    setcookie($cookie_name, $cookie_value, $expiration, "/");

    if (isset($_COOKIE["user"])) {
        $cookie_value = $_COOKIE["user"];
        echo "Welcome, $cookie_value!";
    } else {
        echo "Cookie not set.";
    }

    // Deletion of cookie
    $cookie_name = "user";
    $expiration = time() - 3600;
    setcookie($cookie_name, "", $expiration, "/");
?>