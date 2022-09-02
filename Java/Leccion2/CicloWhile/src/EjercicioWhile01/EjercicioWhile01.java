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
        // CICLO FOR con break
        for(var contar = 0; contar < 7; contar++){
            if (contar % 2 == 0){ // va a imprimir los numeros pares
            System.out.println("contar = " + contar);//imprime de 0 A 6
            break; // solo va a mostrar el 0, sin el break muestra el 0,2,4 y 6
            }
        }
        // Palabra reservada continue
        for(var contar = 0; contar < 7; contar++){
            if (contar % 2 != 0){ // va a imprimir los numeros impares
            continue; // va a la siguiente iteracion, vuelve al ciclo, cada vez que encuentra un numero impar vuelve al ciclo, si encuentra un numero par sale del ciclo y imprime los numeros pares
            }
            System.out.println("contar = " + contar); // va a imprimir 0,2,4,6
        }
         // Etiqueta Labels (no es recomendable su uso, puede romper la logica)se trabaja con las palabras break y continue
         inicio:
         for(var contar = 0; contar < 7; contar++){
            if (contar % 2 == 0){ // va a imprimir los numeros pares
            System.out.println("contar = " + contar); // va a imprimir el mismo resultado 0
            break inicio; // vuelve al inicio
            }
            
        }
        
    }  
}
