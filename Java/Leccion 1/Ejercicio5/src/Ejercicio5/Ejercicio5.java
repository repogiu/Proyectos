// Hacer un programa que calcule e imprima la suma de tres calificaciones
//Pedir las calificaciones al usuario, crear un proyecto nuevo llamado Ejercicio 5
package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float nota1,nota2,nota3,suma;
        
        System.out.println("Digite las tres calificaciones: ");
        nota1 = Float.parseFloat(entrada.nextLine()); // conversion del dato provisto por el usuario a tipo float
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());
        suma = nota1 + nota2 + nota3;
        
        System.out.println("\nLa suma de las calificacioes es = " + suma); // imprime un salto de linea entre la ultima nota y la suma
        
        
        
    }
}