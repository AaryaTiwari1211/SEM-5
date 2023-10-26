<?php
    if($_SERVER["REQUEST_METHOD"] == "POST")
    {
        $name = $_POST['name'];
        $age = $_POST["age"];
        $gay = $_POST["gay"];

        if(empty($name) || empty($age) || empty($gay))
        {
            echo "Please fill all fields!!";
        }
        else
        {
            setcookie("cookie1" , $name , time() + 60);
            setcookie("cookie2" , $age , time() + 60);
            setcookie("cookie3" , $gay , time() + 60);
            if(isset($_COOKIE["cookie1"]) && isset($_COOKIE["cookie2"]) && isset($_COOKIE["cookie3"]))
            {
                echo "Name is: $name <br>"; 
                echo "Age is: $age <br>"; 
                echo "IS Gay?: $gay <br>"; 
                // header("Location: cookie2.php");
            }
            else
            {
                echo "Cookies are not set!!";
            }
        }
    }
?>