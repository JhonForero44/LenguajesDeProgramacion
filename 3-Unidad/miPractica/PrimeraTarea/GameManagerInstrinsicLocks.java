package PrimeraTarea;

import java.util.Scanner;

public class GameManagerInstrinsicLocks {
    // Variable que corresponde al recurso que usa la seccion critica
    static int coins = 10000;

    // candado intrínseco elegido por nosotros
    private final Object lock = new Object();

    void consumirMonedas(int cantidadMonedas) {
        synchronized (lock) {
            if (coins >= cantidadMonedas) {
                coins -= cantidadMonedas;
                System.out.println("Hilo " + Thread.currentThread().getName()
                        + " consumió: " + cantidadMonedas
                        + " | Restantes: " + coins);
            } else {
                System.out.println("No hay suficientes monedas para consumir "
                        + cantidadMonedas);
            }
        }
    }

    public static void main(String[] args) {

        // Pedir numero de jugadores
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Ingresa el numero de jugadores: ");
        int numeroJugadores = scanner.nextInt();

        // Iniciar los hilo para cada jugador
        Thread[] threads = new Thread[numeroJugadores];

        // Crear una instancia compartida que será el recurso/monitor
        GameManagerInstrinsicLocks gm = new GameManagerInstrinsicLocks();

        // Cada hilo consume una cantidad de monedas
        for (int i = 0; i < numeroJugadores; i++) {
            int coinsConsumidas = (int) (Math.random() * 100) + 1;
            // Crear el hilo
            threads[i] = new Thread(() -> {
                try {
                    Thread.sleep((int) (Math.random() * 50));
                } catch (Exception e) {
                }
                gm.consumirMonedas(coinsConsumidas);
            });
        }

        // Iniciar cada hilo
        for (int i = 0; i < numeroJugadores; i++) {
            threads[i].start();
        }

        // Terminar cada hilo
        for (int i = 0; i < numeroJugadores; i++) {
            try {
                threads[i].join();
            } catch (Exception e) {
                // TODO: handle exception
            }
        }

        // Al final debe imprimirse el balance final de monedas
        System.out.println("Monedas restantes: " + GameManagerInstrinsicLocks.coins);

        // Cerar Scanner
        scanner.close();
    }
}
