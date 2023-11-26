<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Experiment 8</title>
</head>

<body>

    <form>
        <input type="text" name="empId" id="empId" placeholder="Enter Employee ID">
        <input type="submit" value="Submit">
    </form>
    <?php
    if (isset($_GET['empId'])) {
        $empId = $_GET['empId'];
        $url = "http://localhost/WP2/EXP8/rest.php/?id=" . $empId;
        $client = curl_init();
        curl_setopt_array($client, [
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_URL => $url
        ]);
        $result = curl_exec($client);
        curl_close($client);
        echo "Response from the server";
        print_r($result);
    }

    ?>
</body>

</html>