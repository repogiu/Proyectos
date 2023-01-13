/*
Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar
la suma de todos los números introducidos.
*/
package Ciclos06;

import java.util.Scanner;


public class Ciclos06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero,suma = 0;
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma+= numero;
        }while(numero != 0); // este ciclo va a trabajar mientras el numero introducido por el usuario sea diferente de 0
        // fuera del ciclo do while mostramos los datos del usuario
        System.out.println("\nLa suma de todos los numeros ingresados es: "+suma);
    }
    
}
