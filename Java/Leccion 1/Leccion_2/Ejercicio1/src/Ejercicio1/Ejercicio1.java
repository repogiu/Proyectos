// Determinar si un alumno aprueba o reprueba un curso, sabiendo que, aprobó si su promedio 
//de 3 calificaciones es mayor o igual a 70, caso contrario reprueba.
package Ejercicio1;

import java.util.Scanner;


public class Ejercicio1 {
    public static void main(String[] args) {
        
        var entrada = new Scanner(System.in);
        System.out.println("Ingrese nota 1: ");
        int nota1 = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Ingrese nota 2: ");
        int nota2 = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Ingrese nota 3: ");
        int nota3 = Integer.parseInt(entrada.nextLine());
        
        int promedio = (nota1 + nota2 + nota3)/3;
        
        if (promedio >= 70) {
            System.out.println("Usted esta aprobado con = " + promedio);
        }
        else {
            System.out.println("Usted esta reprobado con = " + promedio );
        }
    }
}
