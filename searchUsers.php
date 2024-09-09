<?php

  $server = "localhost";
  $username= "usuario"; //nombre de usuario que se conecta a la base de datos
  $password= "contraseña"; //contraseña del usuario de la base de datos
  $database = "basededatos"; //nombre de la base de datos

  //conexion a la base de datos
  $conn = new mysqli($server, $username, $password, $database);
  //sanitizacion
  $id = mysqli_real_escape_string($conn, $_GET['id']);

 //echo "[+] Tu valor introducido es: " . $id . "<br>---------------------------------------------------------------<br>";

  $data = mysqli_query($conn, "select username from users where id = $id");
  $response = mysqli_fetch_array($data);

  if (!isset($response['username'])){

    http_response_code(404);

  }

?>
