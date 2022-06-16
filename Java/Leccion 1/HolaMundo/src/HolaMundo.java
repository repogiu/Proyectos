
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
         //var entrada = new Scanner(System.in);
         /*System.out.println("Digite su edad:");
         edad = Integer.parseInt (entrada.nextLine());
         System.out.println("edad = " + edad); */
         
         //Conversion de tipos primitivos 2
         
         /*var edadTexto = String.valueOf(10);
         System.out.println("edadTexto = " + edadTexto);
        
         var fraseChar = "programadores".charAt(10);
         System.out.println("fraseChar:" + fraseChar);
         
         System.out.println ("Digite un caracter: ");
         fraseChar = entrada.nextLine().charAt(0);
         System.out.println("fraseChar = " + fraseChar);*/
         
         /*int num1=5, num2=4;
         var solucion = num1 + num2;
         System.out.println("solución suma = " + solucion);
        
         solucion = num1 - num2;
         System.out.println("solución resta = " + solucion);
        
         solucion = num1 * num2;
         System.out.println("solución multiplicación = " + solucion);
        
         solucion = num1 / num2;
         System.out.println("solución división = " + solucion);
        
         var solucion2 = 3.4 / num2;
         System.out.println("resultado de la división = " + solucion2);
         //no es lo mismo flotanto que float(q es algo de java)
        
         solucion = num1 % num2;//Guarda el residuo entero de la división
         System.out.println("solucion = " + solucion);
         
         if (num1 % 2 == 0) 
             System.out.println("Es un número par");
         else
             System.out.println("Es un número impar");*/
        
        /* int varNum1 = 1, varNum2 = 4;
         int varNum3 = varNum1 + 6 - varNum2;
         System.out.println("varNum3 = " + varNum3);
        
         varNum1 += 1; // varNum1= varNum1 + 1; operador de composición
         System.out.println("varNum1 = " + varNum1);
        
         varNum2 -= 1;
         System.out.println("varNum2 = " + varNum2);
        
         varNum2 *= 2;
         System.out.println("varNum2 = " + varNum2);
         
         varNum2 /= 2;
         System.out.println("varNum2 = " + varNum2);
        
         varNum3 %= 2;
         System.out.println("varNum3 = " + varNum3);*/
        
         //Clase 8: Operadores unarios: cambio de Signo
        /* var varA = 7;
         var varB = - varA;
         System.out.println("varA = " + varA);
         System.out.println("varB = " + varB);//El resultado sera negativo
        
        //Operador de negacion (aplicable a variables tipo boolean)
        var varC = true;//Esta variable por default en Java es de tipo boolean
        var varD = !varC;//Aqui esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores unarios de incrementeo: Preincremento
        var varE = 9;//Se va a modificar su valor
        var varF = ++varE;//Simbolo antes de la variable
        //Primero se incrementa la variable y luego se usa su valor
        System.out.println("varE = " + varE);//Se incrementa en la variable
        System.out.println("varF = " + varF);//Va a sumar uno
                
        //Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++;//Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores unarios de decremento: Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);//La variable I ya esta con decremento
        System.out.println("varJ = " + varJ);
        
        //Postdecremento
        var varK = 8;
        var varL = varK--;//Primero el valor de la varible, luego queda el decremento
        System.out.println("varK = " + varK);//Aqui va a decrementar en 1
        System.out.println("varL = " + varL);
        
        //Operadores de igualdad y relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum ==bNum);//Nos regresa un valor booleano: true o folse - Los parentesis son opcionales
        System.out.println("cNum = " + cNum);
        var dNum = aNum != bNum;//Nos regresa un valor booleano: true o folse
        System.out.println("dNum = " + dNum);
        var cadenaA = "Hello";
        var cadenaB = "Hello";
        var cVar = cadenaA == cadenaB;//No hace una comparacion de lo que hay adentro, sino que de las referencias de objetos
        System.out.println("cVar = " + cVar);
        var fVar = cadenaA.equals(cadenaB);//Aca si hace la comparacion de lo que tiene guardadado dentro de las variables string
        System.out.println("fVar = " + fVar);
        
        //Operadores relacionales
        var gVar = aNum >= bNum;//< <= > >= == !=
        System.out.println("gVar = " + gVar);
        //Se puede poneer parentesis o no
        
        if(aNum % 2 == 0){
            System.out.println("El numero es par");
        }else{
            System.out.println("El numero es impar");
        }//Es aconsejable utilizar las llaves para evitar que se rompa el codigo
        
        var edad = 30;
        var adulto = 18;
        if(edad >= adulto){
            System.out.println("Es mayor de edad");
        }else{
            System.out.println("Es menor de edad");
        }*/
        //Operadores condicionales: And
        /*var valorA = 7;
        var valorMinimo = 0;//Rango del 0 al 10
        var valorMaximo = 0;
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        //Operador Or
        var vacaciones = false;
        var diaLibre = true;
        if (vacaciones || diaLibre) {
            System.out.println("El papa puede asistir al juego de su hijo");
        } else {
            System.out.println("El papa no puede asistir al juego de su hijo");
        }*/
        
        //Operador Ternario (se recomienda con expresiones sencillas, de lo contrario utilizamos la estructura if/else))
        /*var resultadoT = (5 > 8) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);*/
        
        //Prioridad de los operadores
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16
        
        var solucionAritmetica = 4 + 5 * 6 / 3;// 4 + ((5 * 6) / 3) = 30 / 3 = 10 + 4 =
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4+5) * 6 / 3;// 4 + 5 = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
    
    
    
    
    
  
        
        
        
        
        
        
        
        
        
        
        
        
    }
    
}