package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in); 
       float dGuillermo,dLuis,dJuan,dTotal;
       
       System.out.println("Digite la cantidad de dolares de Guillermo: ");
       dGuillermo = Float.parseFloat(entrada.nextLine());
       dLuis = dGuillermo / 2;
       dJuan = (dGuillermo + dLuis) / 2;
       dTotal = dGuillermo + dLuis + dJuan;
        System.out.println("El total de dolares es: "+dTotal);
        System.out.println("El total de dolares de Luis es: "+dLuis);
        System.out.println("El total de dolares de Juan es: "+dJuan);
       
       
       
    }
}