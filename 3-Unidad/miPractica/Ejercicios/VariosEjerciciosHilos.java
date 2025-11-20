package Ejercicios;
import java.util.concurrent.atomic.AtomicInteger;

public class VariosEjerciciosHilos {

}

class Ejercicio1 {

    public static void main(String[] args) {

        int numeroHilos = 5;

        Thread[] threads = new Thread[numeroHilos];

        for (int i = 0; i < numeroHilos; i++) {

            threads[i] = new Thread(() -> {

                Thread hilo = Thread.currentThread();

                System.out.println("Nombre del hilo: " + hilo.getName());

                try {
                    Thread.sleep(400);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        }

        // Inicio
        for (Thread t : threads)
            t.start();

        // Esperar
        for (Thread t : threads) {
            try {
                t.join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

class Ejercicio2 {
    /*
     * Ejercicio: Cajero Bancario Sincronizado
     * Objetivo
     * - Simular varios hilos retirando dinero desde la misma cuenta bancaria.
     * - Usar synchronized para evitar que dos hilos retiren al mismo tiempo y
     * evitar que el saldo se vuelva negativo.
     * 
     * Descripción del ejercicio
     * - Tienes una cuenta con un saldo inicial, por ejemplo: 1000.
     * - Creas 3 hilos, cada uno intentando retirar 400.
     * - Sin sincronización, podría quedar saldo negativo.
     * - Con synchronized, solo un hilo a la vez puede realizar el retiro
     * correctamente.
     */

    public static void main(String[] args) {
        // Constantes
        int[] saldoInicial = { 1000 };
        int valorRetirar = 400;

        // Numero de hilos
        int numeroHilos = 3;

        // Crear un arreglo de hilos
        Thread[] thread = new Thread[numeroHilos];

        // Crear Hilo
        for (int i = 0; i < numeroHilos; i++) {
            thread[i] = new Thread(() -> {
                Thread hilo = Thread.currentThread();
                if (saldoInicial[0] > valorRetirar) {
                    saldoInicial[0] -= valorRetirar;
                    System.out.println("Hilo: " + hilo.getName() + "retiro $400, saldo actual: " + saldoInicial[0]);
                } else {
                    System.out.println("Hilo: " + hilo.getName() + "no puede retirar, saldo insuficiente");
                }
            });
        }

        // Iniciar hilo
        for (int i = 0; i < numeroHilos; i++) {
            thread[i].start();
        }

        // Finalizar Hilo
        for (int i = 0; i < numeroHilos; i++) {
            try {
                thread[i].join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        // Esto global de las monedas
        System.out.println("Saldo final en la cuenta: " + saldoInicial[0]);
    }
}

class Ejercicio3 {
    /*
     * Objetivo
     * Simular varios usuarios (hilos) entrando a una página web y aumentando un
     * contador de visitas.
     * 
     * Sirve para entender:
     * Condiciones de carrera (race conditions)
     * Qué pasa si varios hilos modifican el mismo valor a la vez
     * Cómo usar synchronized (o no usarlo primero para observar el error)
     * 
     * 📝 Descripción del ejercicio: SIN SINCRONIZAR
     * Hay un contador global llamado visitas.
     * Creas 10 hilos, cada uno simula que un usuario "entra" a la página 100 veces
     * Cada entrada incrementa el contador en 1.
     * Sin sincronización, el resultado será incorrecto (porque se pierden
     * incrementos).
     * Con sincronización, el contador final será exactamente 1000.
     * 
     */

    static int visitas = 0;

    public static void main(String[] args) {
        // Numero de Hilos
        int numHilos = 5;
        int ingresoPaginas = 1000;

        // Crear arreglos de hilos
        Thread[] threads = new Thread[numHilos];

        // Crear cada uno de los hilos
        for (int i = 0; i < numHilos; i++) {
            int idHilo = i; 
            threads[i] = new Thread(() -> {
                for (int j = 0; j < ingresoPaginas; j++) {
                    visitas++;
                    System.out.println("Hilo " + idHilo + " incrementó visitas a: " + visitas);
                }
            });
        }

        // Empezar Hilos
        for (int i = 0; i < numHilos; i++) {
            threads[i].start();
        }

        // Terminas Hilos
        for (int i = 0; i < numHilos; i++) {
            try {
                threads[i].join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        // Imprimir visitas finales
        System.out.println("Visitas finales: " + visitas);

    }
}

class Ejercicio4 {
    /*
     * Objetivo
     * Simular varios usuarios (hilos) entrando a una página web y aumentando un
     * contador de visitas.
     * 
     * Sirve para entender:
     * Condiciones de carrera (race conditions)
     * Qué pasa si varios hilos modifican el mismo valor a la vez
     * Cómo usar synchronized (o no usarlo primero para observar el error)
     * 
     * 📝 Descripción del ejercicio: SIN SINCRONIZAR
     * Hay un contador global llamado visitas.
     * Creas 10 hilos, cada uno simula que un usuario "entra" a la página 100 veces
     * Cada entrada incrementa el contador en 1.
     * Sin sincronización, el resultado será incorrecto (porque se pierden
     * incrementos).
     * Con sincronización, el contador final será exactamente 1000.
     * 
     */

    static int visitas = 0;

    public static synchronized void incrementar() {
        visitas++;
    }

    public static void main(String[] args) {
        // Numero de Hilos
        int numHilos = 10;
        int ingresoPaginas = 1000;

        // Crear arreglos de hilos
        Thread[] threads = new Thread[numHilos];

        // Crear cada uno de los hilos
        for (int i = 0; i < numHilos; i++) {
            int idHilo = i; 
            threads[i] = new Thread(() -> {
                for (int j = 0; j < ingresoPaginas; j++) {
                    incrementar();
                    System.out.println("Hilo " + idHilo + " incrementó visitas a: " + visitas);
                }
            });
        }

        // Empezar Hilos
        for (int i = 0; i < numHilos; i++) {
            threads[i].start();
        }

        // Terminas Hilos
        for (int i = 0; i < numHilos; i++) {
            try {
                threads[i].join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        // Imprimir visitas finales
        System.out.println("Visitas finales: " + visitas);

    }
}

class Ejercicio5{
    // import java.util.concurrent.atomic.AtomicInteger;
    /*
     * Objetivo:
     * Simular varios usuarios (hilos) entrando a una página y aumentando un contador
     * de visitas usando AtomicInteger.
     *
     * Con AtomicInteger:
     * - No necesitas synchronized.
     * - No hay condiciones de carrera.
     * - El resultado final siempre será correcto.
     */

    static AtomicInteger visitas = new AtomicInteger(0);

    public static void main(String[] args) {

        int numHilos = 10;
        int ingresoPaginas = 1000;

        Thread[] threads = new Thread[numHilos];

        // Crear hilos
        for (int i = 0; i < numHilos; i++) {

            int idHilo = i;  

            threads[i] = new Thread(() -> {

                for (int j = 0; j < ingresoPaginas; j++) {

                    int nuevoValor = visitas.incrementAndGet();

                    System.out.println(
                        "Hilo " + idHilo +
                        " incrementó visitas → " + nuevoValor
                    );
                }

            });
        }

        // Iniciar hilos
        for (int i = 0; i < numHilos; i++) {
            threads[i].start();
        }

        // Esperar a que terminen
        for (int i = 0; i < numHilos; i++) {
            try {
                threads[i].join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        System.out.println("\nVisitas finales: " + visitas.get());
    }
}
