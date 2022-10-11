<?php 
// Arreglos de Indice numerico

$frutas=array("manzanas","pera","mandarina","banana");
print_r($frutas);
echo "<br/>";
//Letura
echo $frutas[0]."<br/>";
echo $frutas[1]."<br/>";
echo $frutas[2]."<br/>";
echo $frutas[3]."<br/>";

echo "<br/>";
// impresion con ciclo for
for($i=0;$i<4;$i++) {  
    echo $frutas[$i]."<br/>";
}  

?>