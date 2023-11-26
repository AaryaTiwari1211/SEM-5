<?php
$data = array(
    array("id" => 1, "name" => "Dhruv Sharma", "age" => 22),
    array("id" => 2, "name" => "Pratham Goenka", "age" => 23),
    array("id" => 3, "name" => "Aarya Tiwari", "age" => 24),
    array("id" => 4, "name" => "Dhairya Satra", "age" => 25),
    array("id" => 5, "name" => "Priyanshi Varshney", "age" => 26)
);
$id = $_GET['id'];

echo json_encode($data[$id - 1], JSON_PRETTY_PRINT);
?>  