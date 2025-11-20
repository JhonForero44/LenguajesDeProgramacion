package PrimeraActividad;

import java.util.Scanner;

public class GameManagerMetodoSincronizar {
    // Variable que corresponde al recurso que usa la seccion critica
    private int coins = 10000;

    synchronized void consumirMonedas(int cantidadMonedas) {
        if (coins >= cantidadMonedas) {
            coins -= cantidadMonedas;
            System.out.println("Hilo " + Thread.currentThread().getName() + " consumió: " + cantidadMonedas
                    + " | Restantes: " + coins);
        } else {
            System.out.println("No hay suficientes monedas para consumir "
                    + cantidadMonedas);
        }
    }

    public int getCoins() {
        return coins;
    }

    public static void main(String[] args) {

        // Pedir numero de jugadores
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Ingresa el numero de jugadores: ");
        int numeroJugadores = scanner.nextInt();

        // Iniciar los hilo para cada jugador
        Thread[] threads = new Thread[numeroJugadores];

        // Crear una instancia compartida que será el recurso/monitor
        GameManagerMetodoSincronizar gm = new GameManagerMetodoSincronizar();

        // Cada hilo consume una cantidad de monedas
        for (int i = 0; i < numeroJugadores; i++) {
            int coinsConsumidas = (int) (Math.random() * 100) + 1;
            // Crear el hilo
            threads[i] = new Thread(() -> {
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
                e.printStackTrace();
            }
        }

        // Al final debe imprimirse el balance final de monedas
        System.out.println("Monedas restantes: " + gm.getCoins());
        // Cerar Scanner
        scanner.close();
    }
}
