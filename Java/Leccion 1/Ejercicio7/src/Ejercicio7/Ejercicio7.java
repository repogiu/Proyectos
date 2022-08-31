//Una compañia de venta de carros usados, paga a su personal de ventas un salario de $1000
//mensuales mas una comision de $150 por cada carro vendido, mas el 5% del valor de la venta por carro.
//Cada mes el capturista de la empresa ingresa en la computadora los datos pertinentes.
//Hacer un programa que calcule e imprima el salario mensual de un vendedor dado.
//El salario de 1000 lo vamos a manejar como un dato constante, para asignarlo debemos usar la palabra reservada "final"
package Ejercicio7;
import java.util.Scanner;     
public class Ejercicio7 {
    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);
       final int salario = 1000; //SUELDO BASICO
       int comision = 150;      //tbm se puede poner int comision=150,cantAuto;
       float salMensual, precioAuto, porcVenta;
       int cantAuto;
       
        System.out.println("Digite la cantidad de autos vendidos: ");
        cantAuto = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del auto: ");
        precioAuto = Float.parseFloat(entrada.nextLine());
        
        comision *= cantAuto;
        porcVenta = precioAuto * cantAuto * 0.05f;
        salMensual = salario + comision + porcVenta;
        
        System.out.println("El salario es de: " + salMensual);
    }
}