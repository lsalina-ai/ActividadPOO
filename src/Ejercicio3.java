public class Ejercicio3 {

    public static void main(String[] args) {

        double horas;
        double valorHora;
        double salarioBruto;
        double retencion;
        double salarioNeto;

        horas = 48;
        valorHora = 5000;

        salarioBruto = horas * valorHora;

        retencion = salarioBruto * 12.5 / 100;

        salarioNeto = salarioBruto - retencion;

        System.out.println("SALARIO BRUTO: $" + salarioBruto);
        System.out.println("RETENCION EN LA FUENTE: $" + retencion);
        System.out.println("SALARIO NETO: $" + salarioNeto);

    }

}