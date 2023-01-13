
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a; // el valor asignado por default es 0, un booleano siempre por default es false
    int b;
    
    //Metodos de la clase 
    public void sumarNumeros(){
        int resultado = a + b; // resultado es una variable local, se destruye una vez que se ejecuta el programa
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;
    }
    
    public int sumarConArgumentos(int a, int b){
        this.a = a;
        this.b = b;
        //return a + b;
        return this.sumarConRetorno();
    }
    
}
