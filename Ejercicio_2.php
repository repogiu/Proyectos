<?php 
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