// En un almacen se hace un 20 % de descuento a los clientes cuya compra
//supere los 100 pesos. Cual sera la cantidad que pagara una persona por
//su compra?
package Ejercicio2;

import java.util.Scanner;


public class Ejercicio2 {
    public static void main(String[] args) {
        var entrada = new Scanner(System.in);
        System.out.println("Ingrese el monto total de la compra: ");
        int compra = Integer.parseInt(entrada.nextLine());
        
        if (compra > 100) {
            float descuento = (float) (compra*0.2);
            float precio = compra - descuento;
            System.out.println("Su compra es = $" + precio);
        }
        else {
            System.out.println("Su compra es = $ " + compra);
        }
    }
}
