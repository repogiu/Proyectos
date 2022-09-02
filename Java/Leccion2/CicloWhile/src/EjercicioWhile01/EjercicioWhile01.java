// CICLOS
// ciclo while (mientras hacer)
package EjercicioWhile01;

public class EjercicioWhile01 {
   public static void main(String[] args) {
        var conteo = 0;
        while (conteo < 7) {
            System.out.println("conteo = " + conteo); // imprime de 0 a 6
            conteo++; // aumentamos en 1 la variable
        }
        
        // ciclo do while ( Repetir hasta)
        var contador = 0;
        do { // se va a ejecutar 1 vez
            System.out.println("contador = " + contador); // imprime desde 0 a 6
            contador ++; // para que no se vuelva infinito
        } while(contador < 7); // luego va a entrar en la condicion y si es verdadera vuelve a ejecutar, aca se agregar el punto y coma
        // CICLO FOR
        for(var contar = 0; contar < 7; contar++){
            System.out.println("contar = " + contar);//imprime de 0 A 6
            
        }
    }  
}
