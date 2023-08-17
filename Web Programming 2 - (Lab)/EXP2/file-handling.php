<?php
    $file1 = fopen("index1.txt",'r+');
    $file2 = fopen("index2.txt",'w');
    $file3 = fopen("index3.txt",'a');

    $filesize1 = filesize("index1.txt");
    $filesize2 = filesize("index2.txt");
    $filesize3 = filesize("index3.txt");

    $filedata1 = fread($file1, $filesize1);
    $filedata2 = fread($file2, $filesize2);
    $filedata3 = fread($file3, $filesize3);

    echo $filedata1 . "<br>";
    echo $filedata2 . "<br>";
    echo $filedata3 . "<br>";

    $file = fopen("index1.txt", 'r+');
    $text = "Dev Dev Dev Dev Dev Dev Dev Dev\n";
    fwrite($file, $text);
    $filesize = filesize("index1.txt");

    $filedata = fread($file, $filesize1);

    echo $filedata;

?>