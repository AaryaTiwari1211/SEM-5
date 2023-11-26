<?php
    header("Content-Type: image/png");
    $im = @imagecreate(500,500)
    or die("Cannot Initialize new GD image stream");
    $background_color = imagecolorallocate($im, 255, 255, 255);
    $text_color = imagecolorallocate($im, 14, 233, 91);
    imagestring($im, 5, 200, 200, "Dev Dev Dev Dev Dev", $text_color);
    imagepng($im);
    imagedestroy($im);
?>
