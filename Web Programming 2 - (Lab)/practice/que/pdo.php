<?php
$host = "localhost";
$username = "root";
$password = "";
$dbname = "test2";

    try {
        $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        echo "Error" . $e->getMessage();
    }

    //Retrieval of data
    try {
        $id = 1;
        $stmt = $conn->prepare("SELECT * from student where id=:id");
        $stmt->bindParam(":id", $id, PDO::PARAM_INT);
        $stmt->execute();
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        echo "Name:". $result["name"] ."Age:". $result["age"];
        print_r($result);
    }
    catch (PDOException $e) {
        echo "Error". $e->getMessage();
    }
    
    try {
        $id = 1;
        $stmt = $conn->prepare("SELECT * from student where id= :id");
        $stmt->bindParam(":id", $id, PDO::PARAM_INT);
        $stmt->execute();
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        // echo "Name:". $result["name"] ."Age:". $result["age"];
        print_r($result);
    }
    catch (PDOException $e) {
        echo "Error". $e->getMessage();
    }


?>