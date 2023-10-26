<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = $_POST["name"];
        $age = $_POST["age"];

        $error = [];

        if (empty($name)) {
            $error[] = "Name is required";
        }
        if (empty($age)) {
            $error[] = "Age is required";
        }

        if (count($error) == 0) {
            echo "" . $name . "";
            echo "" . $age . "";
        } else {
            foreach ($error as $msg) {
                echo "" . $msg . "";
            }
        }

        $cookie_name = "cookie1";
        $cookie_value = $name;
        setcookie($cookie_name,$cookie_value,time()+ 5,"/");

        if(isset($_COOKIE[$cookie_name])) {
            print($_COOKIE[$cookie_name]);
        }
        else {
            echo "Cookie not set";
        }
    }

?>