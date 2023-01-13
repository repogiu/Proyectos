
package Clases;
// la clase debe ser publica para poder acceder desde otros archivos
// el nombre de la clase esta en escritura Pascal case (HolaMundo)
public class Persona {
      //Atributos de la clase (Caracteristicas)
    String nombre;
    String apellido;
    
    //Métodos de la clase (Acciones): reutilizables, se pueden llamar las veces que sean necesarios 
   
    //public: el metodo puede usarse fuera de la clase
    // void: indica que no regresa ningun tipo de inf
    //(): argumentos, indica que podemos recibir inf
    public void obtenerInformacion(){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
    }
    
}
