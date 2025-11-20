package ExplicacionJavaOracle;

/*
Cuando varios hilos acceden a una misma variable o mismo objeto, pueden ocurrir
condiciones de carrera.
Para evitarlo, Java permite sincronizar un método o un bloque de código.

“Solo un hilo a la vez puede entrar a este método o bloque.”
Imagina una puerta con candado:
•Un hilo entra → cierra la puerta
•Termina → abre la puerta para el siguiente
*/

class Contador {
    int valor = 0;

    synchronized void incrementar() { // Sincronizado
        // void incrementar() { //NO sincronizado
        valor++;
        System.out.println("Hilo: " + Thread.currentThread().getName() + " incrementó a: " + valor);
    }
}

/*
 * Sincronizar por bloque
 * class Contador {
 * int valor = 0;
 * void incrementar() {
 * synchronized (this) {
 * valor++;
 * }
 * }
 * }
 * 
 */

public class MetodoSincronizar {
    public static void main(String[] args) throws Exception {
        Contador c = new Contador();

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++)
                c.incrementar();
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++)
                c.incrementar();
        });

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println("Resultado: " + c.valor);
    }
}