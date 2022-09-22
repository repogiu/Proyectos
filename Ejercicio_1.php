<!--Hacer un programa que muestre un mensaje. Ilustre como incrustar codigo PHP en un doc HTML y como imprimir desde php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Incrustar php en html</title>
    <script type="text/javascript">
        alert("alerta sin php");
    </script>
</head>
<body>
    <h2>Programa que muestra un mensaje</h2>

    <?php 
    echo "Buenos dias";
    print"<h4>Titulo H4 en php</h4>";
    echo "<hr>"; #imprime una linea
    ?>


    <h4>Titulo H4 en html</h4>
   <h2 <?php echo "style='color:blue'";?>>Texto azul</h2>

   <hr> <!-- este hr es una linea horizontal, que divide -->
   
   <h3>Mostramos el ejercicio 3</h3> <!-- h eader -->

   
    <?php 
    //programa que calcula una tabla de multiplicar. Ilustra como manejar variables y como usar bucles

    $tablaInicial = 1;
    $tablaFinal = 9;

    for($tabla=$tablaInicial; $tabla<=$tablaFinal;$tabla++) {
        echo "Tabla del ". $tabla. "<br>". "<br>";
        for($i=1; $i<=10; $i++) {
            $resultado = $i * $tabla;
            echo $tabla. " * ". $i. " = ". $resultado. "<br>";
        }
        echo "<br>";

    }
    ?>

    
</body>
</html>