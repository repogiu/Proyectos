
<?php 
//programa que calcula una tabla de multiplicar. Ilustra como manejar variables y como usar bucles

$tablaInicial = 1;
$tablaFinal = 10;

for($tabla=$tablaInicial; $tabla<=$tablaFinal;$tabla++) {
    echo "Tabla del ". $tabla. "<br>". "<br>";
    for($i=1; $i<=10; $i++) {
        $resultado = $i * $tabla;
        echo $tabla. " * ". $i. " = ". $resultado. "<br>";
    }
    echo "<br>";

}
?>