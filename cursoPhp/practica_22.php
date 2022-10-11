<?php 
// Arreglo asociativo: declarar arreglos con indice no numerico

$frutas=array("f"=>"frutilla", "m"=>"manzana", "p"=>"pera");
print_r($frutas);
echo $frutas["f"]."<br/>";
echo $frutas["m"]."<br/>";
echo $frutas["p"]."<br/>";

echo "<br/>";

// imprimir con ciclo foreach: vamos a leer frutas, le vamos a pasar como indice un valor
foreach($frutas as $indice => $valor) { 
    echo $indice."<br/>"; // imprime f,m y p

}
echo "<br/>";

foreach($frutas as $indice => $valor) { 
    echo $valor."<br/>"; // imprime frutilla, manzana y pera

} 

echo "<br/>";

foreach($frutas as $indice => $valor) { 
    echo "El valor ".$valor." tiene el indice: ".$indice."<br/>"; 

}
?>