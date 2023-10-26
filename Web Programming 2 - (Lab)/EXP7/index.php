<?php
require '../vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require_once '../vendor/phpmailer/phpmailer/src/Exception.php';
require_once '../vendor/phpmailer/phpmailer/src/PHPMailer.php';
require_once '../vendor/phpmailer/phpmailer/src/SMTP.php';

$mail = new PHPMailer(true);

try {
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587;

    $mail->Username = 'aarya.tiwari@somaiya.edu';
    $mail->Password = 'Aarya@2003';

    $mail->setFrom('aarya.tiwari@somaiya.edu', 'Aarya Tiwari');
    $mail->addAddress('aarya.tiwari@somaiya.edu', 'Aarya Tiwari');
    $mail->addReplyTo('aarya.tiwari@somaiya.edu', 'Aarya Tiwari');

    $mail->IsHTML(true);
    $mail->Subject = "Mail dekho mail";
    $mail->Body = 'Heyyy cutie';
    $mail->AltBody = 'Heyyy cutie';
    $mail->send();
    echo "Email message sent.";
} catch (Exception $e) {
    echo "Error in sending email. Mailer Error: {$mail->ErrorInfo}";
}
?>