<?php 
// Metodo estaticos: pueden llamarse sin tener una instancia (objeto)
class clase {

    public static function metodo() {
        echo "Hola soy un metodo estatico";
}
}

// con instancia
$objeto = new clase();
$objeto ->metodo();
echo "<br/>";

// sin instancia
clase::metodo();

?>