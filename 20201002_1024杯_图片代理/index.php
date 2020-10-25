<?php
if(isset($_GET["picurl"])){
    $ch = curl_init(explode("&",base64_decode($_GET["picurl"]))[0]);
    curl_setopt($ch, CURLOPT_TIMEOUT,2);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT,2);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_BINARYTRANSFER, 1);
    $data = curl_exec($ch);
    curl_close($ch);
    header("Content-type: image/jpeg");
    print( $data );
    unset($data);
}else{
    header('location:index.php?picurl=aHR0cDovL3AucWxvZ28uY24vZ2gvMzcyNjE5MDM4LzM3MjYxOTAzOC8w');
}