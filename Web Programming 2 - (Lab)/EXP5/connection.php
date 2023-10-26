<?php
$host = 'localhost';
$dbname = 'test2';
$username = 'root';
$password = '';


    
    //Establish connection using PDO
    try {
        $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        echo "Connected successfully!";
    } catch (PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }

    // Filtering Data using PDO
    try {
        $id = 6;
        $stmt = $pdo->prepare("SELECT name, age FROM student WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        $result = $stmt->fetch(PDO::FETCH_ASSOC);

        echo "Name: " . $result['name'] . "<br>";
        echo "Age: " . $result['age'];
    } catch (PDOException $e) {
        echo "Query failed: " . $e->getMessage();
    }

    //Inserting data 
    try {
        $name = "John";
        $age = 25;
        $email = "john@gmail.com";

        $stmt = $pdo->prepare("INSERT INTO student (name, age) VALUES (:name, :age)");
        $stmt->bindParam(':name', $name, PDO::PARAM_STR);
        $stmt->bindParam(':age', $age, PDO::PARAM_INT);
        $stmt->execute();
        echo "Data inserted successfully!";
    } catch (PDOException $e) {
        echo "Insertion failed: " . $e->getMessage();
    }

    // Deleting Data
    try {
        $id = 5;
        $stmt = $pdo->prepare("DELETE from student WHERE id = :id");
        $stmt->bindParam(":id", $id, PDO::PARAM_INT);
        $stmt->execute();
        echo "Data deleted successfully!!";
    }
    catch (PDOException $e) {
        echo "Deleteion failed". $e->getMessage();
    }

?>