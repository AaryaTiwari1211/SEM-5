<?php
    $cookie_name = "user1";
    $cookie_value = "Aarya Tiwari was here";

    function makeCookie($name, $value, $expire, $path)
    {
        setcookie($name, $value, time() + ($expire), "/");
    }
?>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
<body>
    <button type="button" id="startButton" onclick="<?php makeCookie("user1","Aarya Tiwari was here",2,"/")?>">
        Set Cookie
    </button>
    <div id="countdown"></div>
    <script src="script.js"></script>
<?php
    if(!isset($_COOKIE["user1"])) {
        echo "Cookie named " . $cookie_name . " is not set!";
    } else {
        echo "Cookie " . $cookie_name . " is set!<br>";
        echo "Value is: " . $_COOKIE[$cookie_name];
    }
?>

</body>
</html>

