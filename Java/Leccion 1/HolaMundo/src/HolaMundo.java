
import java.util.Scanner;

//Hola Mundo

/**
 *
 * Giuliana Diaz
 */
public class HolaMundo {
    public static void main(String args[]){
       /* System.out.println("Hola Mundo desde Java");
        
        // Reutilizacion de variables
         int miVariable = 10; //Camel Case 
         System.out.println(miVariable); // para no escribir todo: mi espacio
         miVariable = 5; //reutilizacion de variable sin int
         System.out.println(miVariable);// por consola nos muestra el valor de la variable (5)
        
        //Tipo string (no primitivo, es una clase)
        // para definir String como objeto, lo escribimos asi pero asi no es asi
        // String miVariableCadena = new String ("Bienvenidos");
         String miVariableCadena = "Bienvenidos"; // empieza con S mayusculas
         System.out.println(miVariableCadena);
        
        //Reutilizacion de string
         miVariableCadena = "Sigamos creciendo en programacion";
         System.out.println(miVariableCadena);
        */
       //Var - inferencia de tipos en Java
        /* var miVariableEntera2 = 10;
         var miVariableCadena2 = "Seguimos estudiando";
         System.out.println("miVariableCadena2 = " + miVariableCadena2);
       // nos muestra por pantalla miVariableCadena2 = Seguimos estudiando
     
         //soutv + tab
         //Para ejecutar Shift + F6 es la tecla para mayuscula
                  
         
         //Ejercicio de concatenacion
         var usuario = "Osvaldo";
         var titulo = "Ingeniero";
         var union = titulo + " " + usuario;
       
         System.out.println("union = " + union); //imprime por pantalla Ingeniero Osvaldo
         
         var a = 8;
         var b = 4;
         // evalua la expresion de izq a derecha (contexto de cadena)
         System.out.println(a + b); //imprime 12, primero encuentra una variable tipo entera
         System.out.println(usuario + a + b); // imprime Osvaldo84, primero encuentra una variable tipo cadena
         System.out.println(usuario + (a + b)); //imprime Osvaldo 12, cambia la prioridad por los parentesis, concatena la suma con la cadena
       
         //Ejercicio: Caracteres especiales con Java
         var nombre = "Natalia";
         System.out.println("\nNueva linea: \n"+nombre)//imprime un salto de linea entre Natalia y Nueva Linea
         System.out.println("Nueva linea: \n"+nombre); //imprime Nueva linea: (salto de linea) Natalia
         System.out.println("Tabulador: \t"+nombre);   //imprime Tabulador:    Natalia
         System.out.println("\t.:MENÚ:."); //imprime (espacio) .:MENU:.
         System.out.println("\t\t.:MENÚ:."); // el doble de espacio
       
         //Caracter de retroceso
         System.out.println("Retroseso: \b"+nombre); // quita un espacio a la izquierda
         System.out.println("Comillas simples: \'"+nombre+"'"); //imprime: Comillas simples: 'Natalia'
         System.out.println("Comillas Dobles: \""+nombre+"\"");*/
         
         //Clase Scanner; crea un objeto llamado entrada
         /*Scanner entrada = new Scanner(System.in); // inicializa la clase scanner, esta en otro paquete
         System.out.println("Digite su nombre: ");
         var usuario2 = entrada.nextLine(); //metodo tipo string, le pedimos al usuario que nos ingrese un valor a esa variable
         System.out.println("usuario2 = " + usuario2);
         System.out.println("Escriba el titulo: "); 
         var titulo2 = entrada.nextLine();
         System.out.println("Resultado: "+titulo2+" "+usuario2); // imprime Resultado: Profesor Ariel*/
        
         //Ejercicio libro
         /*Scanner scanner = new Scanner(System.in);
    
         System.out.println("Proporciona el título:");
         String titulo = scanner.nextLine(); 
         System.out.println("Proporcione el autor:");
         String autor = scanner.nextLine();
         System.out.println(titulo + " fue escrito por " + autor);*/
        
         //Tipos primitivos
         /*byte numEnteroByte = 10; // el 10 es una literal de tipo byte
         byte numEnteroByte = (byte)129; //conversion de tipo (permite almacenar un numero mayor al rango permitido) // imprimte -127, a eso se lo denomina perdida de precision 
         System.out.println("Valor minimo Byte: "+ Byte.MIN_VALUE); //imprime -128
         System.out.println("Valor maximo Byte: "+ Byte.MAX_VALUE); // imprime 127
     
         short numEnteroShort = 23455;
         short numEnteroShort = (short)32768;
         System.out.println("Numero entero short:"+ numEnteroShort);
         System.out.println("Valor mínimo del short:"+ Short.MIN_VALUE);
         System.out.println("Valor máximo del short:"+ Short.MAX_VALUE);
         
         int numEnteroInt = 982465823;
         int numEnteroInt = (int)2147483648L; // se  agrega L o l al final, imprime el numero en negativo
         System.out.println("Número entero int:"+ numEnteroInt);
         System.out.println("Valor mínimo del int:"+ Integer.MIN_VALUE);
         System.out.println("Valor máximo del int:"+ Integer.MAX_VALUE);
         
         long numEnteroLong = 10;
         long numEnteroLong = 9223372036854775807L; // siempre hay que agregar la L al final porque Java por defoult siempre asigna  los numeros enteros a un tipo de dato int.
         System.out.println("Número entero long:"+ numEnteroLong);
         System.out.println("Valor mínimo del long"+ Long.MIN_VALUE);
         System.out.println("Valor máximo del long" + Long.MAX_VALUE);
         
         float numFloat = 2.23239784565F; // siempre se agrega una F(recomendado) o f al final
         float numFloat = (float)2.23239784565; //conversion a float porque por default los tipos flotantes son de tipo double
         float numFloat = (float)3.4025236E38; // imprime Infinity, el complilador no lo puede interpretar
         System.out.println("Número float:"+ numEnteroLong);
         System.out.println("Valor mínimo del float"+ Float.MIN_VALUE);
         System.out.println("Valor máximo del float"+ Float.MAX_VALUE);
         
         double numDouble = 1.7235825138599289347727D; // no hace falta poner la D
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
         /*char miVariableChar ='a'; // imprime mi VariableChar = a
         System.out.println("miVariableChar: " + miVariableChar);
         // codigo unicode
         char varCaracter = '\u0024'; // imprime simbolo dolar
         System.out.println("varCaracter = " + varCaracter);
         // sistemas decimal
         char vaCaracterDecimal = 36;
         System.out.println("vaCaracterDecimal = " + vaCaracterDecimal);
         char varCaracterSimbolo = '$';
         System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
         //Inferencia de tipo char
         var varCaracter1 = '\u0024';
         System.out.println("varCaracter1 = " + varCaracter);
         var vaCaracterDecimal1 = (char)36; // hacer conversion para que el compilador lo reconozca como char y no como entero
         System.out.println("vaCavarEnteroCharracterDecimal1 = " + vaCaracterDecimal);
         var varCaracterSimbolo1 = '$';
         System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo);
         
         //Conversion de un tipo char a int
         int varEnteroChar = '$'; //imprime 36
         System.out.println("varEnteroChar = " + varEnteroChar);*/
    
    
         // tIPOS BOOLEANOS O BANDERA
        /* boolean varBool = true;
         var varBool = true;
         System.out.println("varBool = " + varBool);
         
         // SENTENCIA IF
         if(varBool){  // poner(varBool==true) es redundante, es un codigo duro
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
         /*var edad = Integer.parseInt("20"); //utilizamos la clase Integer y su metoco parseInt, que convierte una cadena a entero
         System.out.println("edad = " + (edad + 1)); // imprime 20, 21
         var valorPI = Double.parseDouble ("3.1416");
         System.out.println("valorPI = " + valorPI);*/
          
         //Pedir un valor con la clase scanner y su metodo nextLine
         //var entrada = new Scanner(System.in); //inicializamos la clase scanner con su objeto entrada
         /*System.out.println("Digite su edad:");
         edad = Integer.parseInt (entrada.nextLine()); // conversion del dato provisto por el usuario a tipo entero
         System.out.println("edad = " + edad); */
         
         //Conversion de un tipo de dato entero a string
         
         /*var edadTexto = String.valueOf(10);
         System.out.println("edadTexto = " + edadTexto); // imprime 10 pero es una cadena
        
         //Recuperar un caracter de una cadena utilizando el metodo charAt
         var fraseChar = "programadores".charAt(10); // si nos salimos del indice tendremos una excepcion
         System.out.println("fraseChar:" + fraseChar);// si ingresamos desarrolladores me imprime fraseChar: d, podemos ingresar un numero porque la clase scanner es string
         
         System.out.println ("Digite un caracter: ");
         fraseChar = entrada.nextLine().charAt(0); // el error se corrige utilizando el metodo charAt porque no podemos corregir un string a char porque el compilador ya a detectado
         System.out.println("fraseChar = " + fraseChar);*/
         
         // Inicializar multiples variables (no aplica a la inferencia de tipo var)
         // Operadores aritmeticos
         /*int num1=5, num2=4;
         var solucion = num1 + num2;
         System.out.println("solución suma = " + solucion);
        
         solucion = num1 - num2;
         System.out.println("solución resta = " + solucion);
        
         solucion = num1 * num2; // el rdo es entero
         System.out.println("solución multiplicación = " + solucion);
        
         solucion = num1 / num2; // el rdo es entero
         System.out.println("solución división = " + solucion);
        
         var solucion2 = 3.4 / num2; // le asigna un tipo double
         System.out.println("resultado de la división = " + solucion2);
         //no es lo mismo flotante que float(q es algo de java)
        
        // Residuo o modulo de la division.
         solucion = num1 % num2;//Guarda el residuo entero de la división
         System.out.println("solucion residuo = " + solucion);
         
         //Algoritmo par o impar, con residuo igual a 0
         Con una sola linea de codigo dentro del bloque if- else no hace falta llaves
         if (num1 % 2 == 0) // si el residuo es 0 el numero es par.
             System.out.println("Es un número par");
         else 
             System.out.println("Es un número impar");*/
        
         //Operadores de asignacion
        /* int varNum1 = 1, varNum2 = 4;
         int varNum3 = varNum1 + 6 - varNum2; //los operadores suma y resta tiene la misma prioridad, por lo tanto la ejecucion de hara de izq a derecha del signo de asignacion
         System.out.println("varNum3 = " + varNum3);
        
         //Operador de composicion (asignacion)
         varNum1 += 1;  //  es lo mismo que escribir varNum1= varNum1 + 1; 
         System.out.println("varNum1 = " + varNum1); // ahora varNum1 vale 2, porque antes valia 1
        
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
        System.out.println("varE = " + varE);//Se incrementa en la variable E tbm en una unidad, vale 10
        System.out.println("varF = " + varF);//Va a sumar uno, vale 10 tbm
                
        //Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++;//Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG); // vale 4
        System.out.println("varH = " + varH); // vale 3, no llego a asignar la suma de unidad
        
        //Operadores unarios de decremento: Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);//La variable I ya esta con decremento, vale 3
        System.out.println("varJ = " + varJ); // vale 3
        
        //Postdecremento
        var varK = 8;
        var varL = varK--;//Primero el valor de la variable, luego queda el decremento
        System.out.println("varK = " + varK);//Aqui va a decrementar en 1, vale 7
        System.out.println("varL = " + varL); // vale 8
        
        //Operadores de igualdad y relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum ==bNum);//Nos regresa un valor booleano: true o folse - Los parentesis son opcionales
        System.out.println("cNum = " + cNum); // regresa false
        
         var dNum = aNum != bNum; 
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "Hello";
        var cVar = cadenaA == cadenaB;// compara referencias no el contenido de la variable. No hace una comparacion de lo que hay adentro, sino que de las referencias de objetos
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);//Aca si hace la comparacion de lo que tiene guardadado dentro de las variables
        System.out.println("fVar = " + fVar);
        
        //Operadores relacionales //< <= > >= == !=
        var gVar = aNum >= bNum; // los parentesis son opcionales
        System.out.println("gVar = " + gVar);
         
        //es aconsejable siempre usar llaves 
        if(aNum % 2 == 0){
            System.out.println("El numero es par");
        }else{
            System.out.println("El numero es impar");
        }//Es aconsejable utilizar las llaves para evitar que se rompa el codigo
         
         // Algoritmo mayor de edad
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
        
        //Algoritmo rango
        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        //Operador Or
        // Algoritmo para asistir evento
        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre) {
            System.out.println("El papa puede asistir al juego de su hijo");
        } else {
            System.out.println("El papa no puede asistir al juego de su hijo");
        }*/
        
        //Operador Ternario (se recomienda con expresiones sencillas, de lo contrario utilizamos la estructura if/else))
        /*var resultadoT = (5 > 8) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        //Ejercicio par e impar (el operador ternario simplifica el if-else)
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar"; // se reutiliza la variable resultadoT
        System.out.println("resultadoT = " + resultadoT);*/
        
        //Prioridad de los operadores (las expresiones se evaluan de izq a derecha)
        /*var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16, primero le suma 1 a x, luego evalua la expresion y que vale 10 y lo suma a 6 y luego le esta en una unidad la variable y
        
        var solucionAritmetica = 4 + 5 * 6 / 3;// primero multiplica 5*6 y luego lo dividi en 3, y luego le suma 4. 4 + ((5 * 6) / 3) = 30 / 3 = 10 + 4 = 14
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        //Uso de parentesis
        solucionAritmetica = (4+5) * 6 / 3;// 4 + 5 = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);*/
        
        // Calcular el area y perimetro de un rectangulo
        var base = 4;
        var altura = 2;
        var area = base * altura;
        var perimetro = 2 * (area);
        System.out.println("El area del rectangulo es = " + area);
        System.out.println("El perimetro del rectangulo es = " + perimetro);
        
        //Algoritmo mayor de dos numeros
        var num1 = 4;
        var num2 = 6;
        var numMayor = (num1 > num2) ? "es mayor" : "es menor";
        System.out.println("numMayor = " + numMayor);
                
    }
    
}