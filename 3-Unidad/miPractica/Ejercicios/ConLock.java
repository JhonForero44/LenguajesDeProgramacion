package Ejercicios;

public class ConLock {

    static int contador = 0;
    static final Object lock = new Object();

    public static void main(String[] args) {

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                synchronized (lock) {
                    contador++;
                }
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                synchronized (lock) {
                    contador++;
                }
            }
        });

        t1.start();
        t2.start();

        try { t1.join(); t2.join(); } catch (Exception e) {}

        System.out.println("Resultado final (correcto): " + contador);
    }
}

