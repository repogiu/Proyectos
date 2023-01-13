/*
Ejercicio 7: Pedir números hasta que se introduzca uno negativo
y calcular el promedio
*/
package Ciclo07;

import java.util.Scanner;


public class Ciclos07 {
     public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){ //Mientras el numero no sea negativo
            suma += numero; // vamos sumando los numeros que ingresa el usuario
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo==0){
            System.out.println("\nError, La división entre cero no existe");
        }
        else{
            promedio = (float)suma/conteo; //conversion
            System.out.println("\nEl promedio es: "+promedio);
        }
    }
    
}
