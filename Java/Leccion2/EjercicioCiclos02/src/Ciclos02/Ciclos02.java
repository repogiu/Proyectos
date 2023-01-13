/*
Ejercicio 2: Leer un número e indicar si es positivo o
negativo. El proceso se repetira hasta que se introduzca
un cero 0
con la clase JOptionPane
*/
package Ciclos02;
import javax.swing.JOptionPane;


public class Ciclos02 {
    public static void main(String[] args) {
        // el metodo show InputDialog captura el dato del usuario
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if(numero > 0){
                // el metodo showMessageDialog envia un mensaje al usuario, recibe dos parametros(Component parensComponent, Object message)
                JOptionPane.showMessageDialog(null, "El número "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "El número "+numero+" finaliza el programa");
    }
    
}

