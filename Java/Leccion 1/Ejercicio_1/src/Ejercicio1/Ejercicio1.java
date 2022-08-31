//Tienda de libros
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine(); // obtenemos el dato ingresado por el usuario
        System.out.println("Digite el ID del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine()); // convertimos el el id ingresamos como string y lo convertimos a entero
        System.out.println("Digite el precio del libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("El envio es gratis?: ");
        boolean envioGratis = Boolean.parseBoolean(entrada.nextLine());
        
        System.out.println(nombreLibro+" #"+idLibro);
        System.out.println("Precio del libro: $"+precioLibro);
        System.out.println("El envio del libro gratuito es: "+envioGratis);
    }
}
