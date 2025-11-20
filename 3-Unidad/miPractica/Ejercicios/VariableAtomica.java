package Ejercicios;

import java.util.concurrent.atomic.AtomicInteger;

public class VariableAtomica {

    static AtomicInteger contador = new AtomicInteger(0);

    public static void main(String[] args) {

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                contador.incrementAndGet();
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                contador.incrementAndGet();
            }
        });

        t1.start();
        t2.start();

        try { t1.join(); t2.join(); } catch (Exception e) {}

        System.out.println("Resultado final (correcto y eficiente): " + contador.get());
    }
}
