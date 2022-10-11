<?php 
// Metodo constructor: necesita de un metodo para que identifique los atributos en la instancia de la clase

class persona {
    public $nombre; // propiedades
    private $edad;

    // metodo constructor
    function __construct($nvoNombre){
        $this->nombre =$nvoNombre; // igual que la linea 16

    }

    //acciones o metodos 
    public function mostrarNombre($nvoNombre) {   
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

// En la creacion de la instancia de la clase (objeto): le pasamos el nombre dentro de el
$objAlumno=new persona("Giuliana ");

// ya no le pasamos el nombre por un metodo
//$objAlumno->mostrarNombre("Giuliana"); // llamada al metodo asignar
$objAlumno->imprimirNombre(); // llamada al metodo imprimir

