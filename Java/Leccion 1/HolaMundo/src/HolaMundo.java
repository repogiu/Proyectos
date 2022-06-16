
import java.util.Scanner;

//Hola Mundo

/**
 *
 * Giuliana Diaz
 */
public class HolaMundo {
    public static void main(String args[]){
       /* System.out.println("Hola Mundo desde Java");
        
         int miVariable = 10;
         System.out.println(miVariable);
         miVariable = 5;
         System.out.println(miVariable);
         
         String miVariableCadena = "Bienvenidos";
         System.out.println(miVariableCadena);
         miVariableCadena = "Sigamos creciendo en programaciÃ³n";
         System.out.println(miVariableCadena);
        */
       //Var - inferencia de tipos en Java
        /* var miVariableEntera2 = 10;
         var miVariableCadena2 = "Seguimos estudiando";
         System.out.println("miVariableCadena2 = " + miVariableCadena2);
     
         //soutv + tab
         //Para ejecutar Shift + F6 es la tecla para mayuscula
         //Reglas para definir una variable en Java
         
         //var miVariableEjemplo = 45;
         //concatenar
         var usuario = "Osvaldo";
         var titulo = "Ingeniero";
         var union = titulo + usuario;
         System.out.println("union = " + union);
         
         var a = 8;
         var b = 4;
         System.out.println(usuario + a + b);
         
         //Ejercicio: Caracteres especiales con Java
         var nombre = "Natalia";
         System.out.println("Nueva linea: \n"+nombre);
         System.out.println("Tabulador: \t"+nombre);
         System.out.println("\t.:MENÚ:.");
         System.out.println("Retroseso: \b"+nombre);
         System.out.println("Comillas simples: \'"+nombre+"'");
         System.out.println("Comillas Dobles: \""+nombre+"\"");*/
        
         //Clase Scanner
         /*Scanner entrada = new Scanner(System.in);
         System.out.println("Digite su nombre: ");
         var usuario2 = entrada.nextLine();
         System.out.println("usuario2 = " + usuario2);
         System.out.println("Escriba el titulo: ");
         var titulo2 = entrada.nextLine();
         System.out.println("Resultado: "+titulo2+" "+usuario2);*/
        
         //Ejercicio libro
         /*Scanner scanner = new Scanner(System.in);
    
         System.out.println("Proporciona el título:");
         String titulo = scanner.nextLine(); 
         System.out.println("Proporcione el autor:");
         String autor = scanner.nextLine();
         System.out.println(titulo + " fue escrito por " + autor);*/
        
         //Tipos primitivos
         /*byte numEnteroByte = 10;
         System.out.println("Valor minimo Byte: "+ Byte.MIN_VALUE);
          System.out.println("Valor maximo Byte: "+ Byte.MAX_VALUE);
     
         short numEnteroShort = 23455;
         System.out.println("Numero entero short:"+ numEnteroShort);
         System.out.println("Valor mínimo del short:"+ Short.MIN_VALUE);
         System.out.println("Valor máximo del short:"+ Short.MAX_VALUE);
         
         int numEnteroInt = 982465823;
         System.out.println("Número entero int:"+ numEnteroInt);
         System.out.println("Valor mínimo del int:"+ Integer.MIN_VALUE);
         System.out.println("Valor máximo del int:"+ Integer.MAX_VALUE);
         
         long numEnteroLong = 10;
         System.out.println("Número entero long:"+ numEnteroLong);
         System.out.println("Valor mínimo del long"+ Long.MIN_VALUE);
         System.out.println("Valor máximo del long"+ Long.MAX_VALUE);
         
         float numFloat = 2.23239784565F;
         System.out.println("Número float:"+ numEnteroLong);
         System.out.println("Valor mínimo del float"+ Float.MIN_VALUE);
         System.out.println("Valor máximo del float"+ Float.MAX_VALUE);
         
         double numDouble = 1.7235825138599289347727D;
         System.out.println("Número double:"+ numEnteroLong);
         System.out.println("Valor mínimo del double"+ Double.MIN_VALUE);
         System.out.println("Valor máximo del double"+ Double.MAX_VALUE);*/
     
         //Clase 5: Inferencias de tipo var y tipos primitivos
         /*var numEntero = 20;
         System.out.println("numEntero = " + numEntero); 
         var numFloat = 10.0F;
         System.out.println("numFloat = " + numFloat);
         var numDouble = 10.0;
         System.out.println("numDouble = " + numDouble);*/
    
         //Tipos primitivos parte 2
         /*char miVariableChar ='a';
         System.out.println("miVariableChar: " + miVariableChar);
         
         char varCaracter = '\u0024';
         System.out.println("varCaracter = " + varCaracter);
         char vaCaracterDecimal = 36;
         System.out.println("vaCaracterDecimal = " + vaCaracterDecimal);
         char varCaracterSimbolo = '$';
         System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
         var varCaracter1 = '\u0024';
         System.out.println("varCaracter1 = " + varCaracter);
         var vaCaracterDecimal1 = (char)36;
         System.out.println("vaCavarEnteroCharracterDecimal1 = " + vaCaracterDecimal);
         var varCaracterSimbolo1 = '$';
         System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo);
         
         int varEnteroChar = '$';
         System.out.println("varEnteroChar = " + varEnteroChar);*/
    
    
         // tIPOS BOOLEANOS O BANDERA
        /* boolean varBool = true;
         System.out.println("varBool = " + varBool);
    
         if(varBool){
         System.out.println("la bandera es verde");
         } 
         else {
         System.out.println("la bandera es roja");
         }
         
         //Es mayor de edad?
         var edad = 17;
         if (edad >= 18) {
             System.out.println("Eres mayor de edad");
         }
         else {
             System.out.println("Eres menor de edad");
         } */
        
         // CONVERSION DE TIPOS PRIMITIVOS
         /*var edad = Integer.parseInt("20");
         System.out.println("edad = " + (edad + 1));
         var valorPI = Double.parseDouble ("3.1416");
         System.out.println("valorPI = " + valorPI);*/
         
         //Pedir un valor
         var entrada = new Scanner(System.in);
         /*System.out.println("Digite su edad:");
         edad = Integer.parseInt (entrada.nextLine());
         System.out.println("edad = " + edad); */
         
         //Conversion de tipos primitivos 2
         
         var edadTexto = String.valueOf(10);
         System.out.println("edadTexto = " + edadTexto);
        
         var fraseChar = "programadores".charAt(10);
         System.out.println("fraseChar:" + fraseChar);
         
         System.out.println ("Digite un caracter: ");
         fraseChar = entrada.nextLine().charAt(0);
         System.out.println("fraseChar = " + fraseChar);
    
    
    
    
    
  
        
        
        
        
        
        
        
        
        
        
        
        
    }
    
}