import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        double radio;
        double area;
        double circunferencia;

        System.out.print("Digite el radio del circulo: ");
        radio = leer.nextDouble();

        area = Math.PI * Math.pow(radio, 2);

        circunferencia = 2 * Math.PI * radio;

        System.out.println("EL AREA DEL CIRCULO ES: " + area);
        System.out.println("LA LONGITUD DE LA CIRCUNFERENCIA ES: " + circunferencia);

    }

}