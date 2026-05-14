import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        int edJuan;
        int edAlberto;
        int edAna;
        int edMama;

        System.out.print("Digite la edad de Juan: ");
        edJuan = leer.nextInt();

        edAlberto = 2 * edJuan / 3;
        edAna = 4 * edJuan / 3;
        edMama = edJuan + edAlberto + edAna;

        System.out.println("\nLAS EDADES SON:");
        System.out.println("ALBERTO: " + edAlberto);
        System.out.println("JUAN: " + edJuan);
        System.out.println("ANA: " + edAna);
        System.out.println("MAMA: " + edMama);

    }

}