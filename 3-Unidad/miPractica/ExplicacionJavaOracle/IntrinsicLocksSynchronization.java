/*
Intrinsic Locks & Synchronization:
Imagina que cada objeto en Java tiene una llave (un candado) invisible pegada a él.
Cuando un hilo (thread) quiere entrar a una parte crítica del código que usa ese objeto, tiene que ponerse
la llave (adquirir el candado). Mientras la tiene, ningún otro hilo puede usar ese mismo candado: si intentan,
se quedan esperando hasta que el primer hilo libere la llave.

Conceptos clave, en corto:
- Intrinsic lock (candado intrínseco): candado que tiene cada objeto 
  (this tiene uno, la clase Class tiene otro).
- synchronized en métodos: si pones synchronized en un método de instancia,
  el hilo adquiere el candado del objeto (this).
- Si el método es static synchronized, el candado es el de la clase (SomeClass.class).
- Bloque synchronized(obj): eliges explícitamente qué candado usar (útil para “locks” finos).
- Reentrante: un hilo que ya tiene el candado puede volver a adquirirlo (esto evita que un hilo 
  se bloquee a sí mismo si entra dos veces en código sincronizado).
- Cuidado: sincronizar demasiado (granulados grandes) reduce concurrencia; sincronizar 
  mal puede causar deadlock (bloqueo mutuo).
*/
package ExplicacionJavaOracle;

public class IntrinsicLocksSynchronization {

    // ===== Ejemplo 2: Bloque synchronized(obj) usando un candado explícito =====
    static class EjemploBloque {
        private int dato = 0;
        private final Object lock = new Object(); // candado intrínseco elegido por nosotros

        public void incrementar() {
            synchronized (lock) { // toma el candado de 'lock'
                dato++;
                System.out.println("Hilo: " + Thread.currentThread().getName() + " incrementó a: " + dato);
            }
        }

        public int getDato() {
            return dato;
        }
    }

    // ===== MAIN =====
    public static void main(String[] args) throws InterruptedException {

        // --- Ejemplo 2: bloque synchronized(obj) ---
        EjemploBloque bloque = new EjemploBloque();

        Thread t3 = new Thread(() -> {
            for (int i = 0; i < 5000; i++)
                bloque.incrementar();
        });

        Thread t4 = new Thread(() -> {
            for (int i = 0; i < 5000; i++)
                bloque.incrementar();
        });

        t3.start();
        t4.start();
        t3.join();
        t4.join();

        System.out.println("Ejemplo 2 - Valor del dato (bloque synchronized): " + bloque.getDato());
    }
}
