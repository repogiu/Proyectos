<!-- Sentencia Switch -->

<?php
if ($_POST) {
    $boton = $_POST["btn"];
    // la sentencia switch evalua que boton presiona
    switch ($boton) {
        case 1:
            echo "El usuario presiono el boton 1";
            break;
        case 2:
            echo "El usuario presiono el boton 2";
            break;
        case 3:
            echo "El usuario presiono el boton 3";
            break;
    }
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="practica_13.php" method="post">
        <input type="submit" name="btn" value="1">
        <br />
        <input type="submit" name="btn" value="2">
        <br />
        <input type="submit" name="btn" value="3">
    </form>

</body>

</html>