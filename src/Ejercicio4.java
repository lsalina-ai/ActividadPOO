import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        double numero;
        double cuadrado;
        double cubo;

        System.out.print("Digite un numero: ");
        numero = leer.nextDouble();

        cuadrado = Math.pow(numero, 2);
        cubo = Math.pow(numero, 3);

        System.out.println("EL CUADRADO ES: " + cuadrado);
        System.out.println("EL CUBO ES: " + cubo);

    }

}
