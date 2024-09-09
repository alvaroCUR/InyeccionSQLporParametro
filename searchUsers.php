<?php

  $server = "localhost";
  $username= "lyoz";
  $password= "lykoz123";
  $database = "hack4u";

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
