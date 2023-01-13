// creacion de objetos
package Clases;

public class PruebaPersona {
       public static void main(String[] args) { // es para ejecutar el programa hacia la consola
        //Persona persona 1; aqui asignamos a la variable persona1 un tipo clase
        // persona1 = new Persona(); // aqui a la variable persona1 ls estamos instanciando y transformando en un objeto
        // objeto 1
        Persona persona1 = new Persona(); //Llamamos al constructor: permite asignar valores al objeto
        // asignamos valores a los atributos de la clase
        persona1.nombre = "Gael"; //el objeto persona1 va a tener una referencia en memoria un valor hexadecimal que normalmente comienza con 0x
        persona1.apellido = "Diaz"; 
        // llamamos al metodo de la clase persona
        persona1.obtenerInformacion();
        // objeto 2
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2); // se muestra la direccion en memoria que se le asigno al objto2
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion(); // nos muestra null ya que aun no se cargo ningun valor
        persona2.nombre = "Giuliana";
        persona2.apellido = "Diaz";
        persona2.obtenerInformacion();
    }
    
}
