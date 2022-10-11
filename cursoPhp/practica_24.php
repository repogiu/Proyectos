<?php 
// Clases 
// visibilidad de los datos (aplica tanto a propiedades y metodos)
// public: se puede acceder desde cualquier objeti
// private: se puede acceder unicamente desde la clase que lo creo (solo puede ser utilizados por los metodos)
// protected: 

class persona {
    public $nombre; // propiedades
    private $edad;
    //acciones o metodos 
    public function MostrarNombre($nvoNombre) {   
        $this ->nombre =$nvoNombre;
}
public function imprimirNombre(){
   echo "Hola soy ".$this->nombre;
}
public function mostrarEdad(){
    $this->edad=20;
    return $this->edad;
}
}

// creacion de objetos o instancias (son reutilizables)
$objAlumno=new persona();
$objAlumno->MostrarNombre("Giuliana"); // llamada al metodo asignar
$objAlumno->imprimirNombre(); // llamada al metodo imprimir
echo "<br/>";

$objAlumno2=new persona();
$objAlumno2->MostrarNombre("Gael");
$objAlumno2->imprimirNombre();
echo "<br/>";

// impresion de objetos
echo $objAlumno->nombre;
echo "<br/>";
echo $objAlumno2->nombre;

echo "<br/>";
echo $objAlumno2->mostrarEdad();

?>