<?php 
// Herencia

class persona {
    public $nombre; // propiedades
    private $edad;
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

// Herencia: la clase trabajador va a ser heredada de la clase persona
// se crea un trabajador a partir de las caracteristicas de una persona (nombre edad)
// la clase trabajador(clase hija) tiene las mismas propiedades y metodos de la clase persona (clase padre)
class trabajador extends persona{  
    public $puesto;

    public function presentarse(){
        echo "Hola soy ".$this->nombre." y soy ".$this->puesto;
}
}


// creacion de objetos de la clase trabajador
$objTrabajador=new trabajador();
$objTrabajador->mostrarNombre("Giuliana"); // reutilizacion del metodo mostrarNombre de la clase persona en la clase trabajador
$objTrabajador->puesto="estudiante";
$objTrabajador->presentarse();
