package Ejercicio7;
import java.util.Scanner;     
public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
       final int salario = 1000;
       int comision = 150,venta;
       float salMensual, ventaAuto, porcVenta, totalPrecio;
       
        System.out.println("Digite la cantidad de autos vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del auto: ");
        ventaAuto = Float.parseFloat(entrada.nextLine());
        
        comision *= venta;
        totalPrecio = ventaAuto * venta;
        porcVenta = totalPrecio * 0.05f;
        salMensual = salario + comision + porcVenta;
        
        System.out.println("El salario es de: " + salMensual);
    }
}