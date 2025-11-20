package Ejercicios;

public class MetodoSincronizado {

    static int contador = 0;

    public synchronized static void incrementar() {
        contador++;
    }

    public static void main(String[] args) {

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) incrementar();
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) incrementar();
        });

        t1.start();
        t2.start();

        try { t1.join(); t2.join(); } catch (Exception e) {}

        System.out.println("Resultado final (correcto): " + contador);
    }
}
