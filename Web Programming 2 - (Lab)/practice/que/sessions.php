<?php
    session_start();
    $_SESSION["name"] = "Aarya Tiwari";
    $_SESSION["age"] = 23;

    echo $_SESSION["name"];

    session_destroy();
?>