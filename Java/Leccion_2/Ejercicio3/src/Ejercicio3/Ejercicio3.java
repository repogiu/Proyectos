//Leer dos numeros. Si son iguales que los multiplique, si el primer numero
// es mayor que el segundo que lo reste, sino que los sume.
package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
        var entrada = new Scanner(System.in);
        System.out.println("Ingrese dos numeros");
        var num1 = Float.parseFloat(entrada.nextLine());
        var num2 = Float.parseFloat(entrada.nextLine());
        float resultado;
        if (num1 == num2) {
            resultado = num1 * num2;
        } else if (num1 > num2) {
            resultado = num1 - num2;
        } else {
            resultado = num1 + num2;
        }
        System.out.println("El resultado es: " + resultado);
    }
}
