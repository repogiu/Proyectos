/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y
luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos.
 */
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        //Esto genera un número aleatorio del 1 al 100 con la clase Math y la funcion random (es de tipo double) hay que hacer la conversion a tipo entero
        aleatorio = (int)(Math.random()*100); 
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un número mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un número menor");
            }
            else{
                System.out.println("\t¡¡¡FELICIDADES!!! Has adivinado el número");
            }
            conteo++;
        } // cierra el ciclo do
        // repetir el do mientras numero sea diferente de aleatorio
        while(numero != aleatorio);
        System.out.println("\tAdivinaste el número en: "+conteo+" intentos");
    }
    
}
