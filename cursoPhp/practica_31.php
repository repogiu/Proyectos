<?php 
// Valores del input text
// Valores del input radio: selector que permite seleccionar unicamente una opcion
// valores input checkbox: permite seleccionar varias opciones
// valores Select option: menu desplegable. Solo se puede seleccionar una opcion
// valores textarea: permite insertar comentarios



// Declaracion de variables
$txtNombre = "";
$radioLenguaje= "";
$chkphp = "";
$chkhtml = "";
$chkcss = "";
$lsAnime= "";
$txtArea= "";

// if ternario: si hubo informacion ? mostrar : sino vacio
if($_POST){
    $txtNombre = (isset($_POST["txtNombre"])) ? $_POST["txtNombre"] :"";
    $radioLenguaje = (isset($_POST["lenguaje"])) ? $_POST["lenguaje"] :"";

    $chkphp = (isset($_POST["chkphp"])=="si") ?"checked":"";
    $chkhtml = (isset($_POST["chkhtml"])=="si") ?"checked":"";
    $chkcss = (isset($_POST["chkcss"])=="si") ?"checked":"";

    $lsAnime= (isset($_POST["lsAnime"]))?$_POST["lsAnime"]:"";

    $txtArea = (isset($_POST["txtArea"])) ? $_POST["txtArea"] :"";

    // VERIFICAMOS envio de informacion
   // print_r($_POST);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario</title>
</head>
<body>
    <?php if($_POST){ ?>
    <strong>Hola </strong>: <?php echo $txtNombre; ?> <br/>
    <strong>Tu lenguaje es: </strong> <?php echo $radioLenguaje; ?>
    <br/>

    <strong> Estas aprendiendo: </strong> <br/>
    <?php echo ($chkphp=="checked")?"PHP":"";?><br/>
    <?php echo ($chkhtml=="checked")?"HTML":"";?><br/>
    <?php echo ($chkcss=="checked")?"CSS":"";?><br/>
    <strong> Tu anime es: </strong> 
    <?php echo $lsAnime;?> <br/>
    <strong> Tu comentario es: </strong>
    <?php echo $txtArea;?>
    <br/>
    <br/>

    <?php } ?>

<form action="practica_31.php" method="post">
<strong>FORMULARIO</strong> <br/>
<br/>
Nombre: <br/>
<input value="<?php echo $txtNombre; ?>" type="text" name="txtNombre" id="">
<br/>
<br/>

<!-- input radio -->

¿Te gusta?: <br/> 
<!-- checked: muestra el value -->
<br/> php: <input type="radio"  <?php echo($radioLenguaje=="php")?"checked":""; ?> name="lenguaje" value="php" id=""><br/>
<br/> html: <input type="radio" <?php echo($radioLenguaje=="html")?"checked":""; ?> name="lenguaje" value= "html" id=""><br/>
<br/> css: <input type="radio" <?php echo($radioLenguaje=="css")?"checked":""; ?> name="lenguaje" value= "css" id=""><br/>
<br/>
<br/>

<!-- input checkbox: muestra las casillas tildadas -->
¿Que estás aprendiendo?: <br/>
<br/>php: <input type="checkbox" <?php echo $chkphp;?> name="chkphp" value="si" id=""><br/>
<br/>html: <input type="checkbox" name="chkhtml" <?php echo $chkhtml;?> value="si" id=""><br/>
<br/>css: <input type="checkbox" <?php echo $chkcss;?>  name="chkcss" value="si" id=""><br/><br/>

<!-- input select option -->
¿Que anime te gusta?: <br/><br/>
<select name="lsAnime" id="">
<option value="">Ninguna</option>
<option value="naruto" <?php echo ($lsAnime=="naruto")?"selected":"" ?> >Naruto</option>
<option value="bleach" <?php echo ($lsAnime=="bleach")?"selected":"" ?>>Bleach</option>
<option value="dragon" <?php echo ($lsAnime=="dragon")?"selected":"" ?>>Dragón Ball</option>

</select>
<br/>
<br/>
<!-- textarea -->
¿Tienes alguna duda?: <br/>
<textarea name="txtArea" id="" cols="30" rows="10">
<?php echo $txtArea;?>

</textarea>
<br/>
<input type="submit" value="Enviar">

</form>
</body>
</html>