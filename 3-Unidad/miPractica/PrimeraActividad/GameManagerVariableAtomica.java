package PrimeraActividad;
import java.util.Scanner;
//Libreria importar para usar Variaables Atomicas
import java.util.concurrent.atomic.AtomicInteger;

public class GameManagerVariableAtomica {
    // Variable compartida entre todos los hilos (segura sin sincronización)
    static AtomicInteger coins = new AtomicInteger(10000);

    public static void main(String[] args) {
        
        //Pedir numero de jugadores 
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Ingresa el numero de jugadores: ");
        int numeroJugadores = scanner.nextInt();

        //Iniciar areglo de los hilo  
        Thread[] threads = new Thread[numeroJugadores];

        // Crear hilos
        for (int i = 0; i < numeroJugadores; i++) {

            // Cada jugador consumirá entre 1 y 100 monedas
            int coinsConsumidas = (int) (Math.random() * 100) + 1;

            threads[i] = new Thread(() -> {

                // Operación atómica para restar
                coins.getAndAdd(-coinsConsumidas);

                // Imprimir info del hilo
                System.out.println(
                    Thread.currentThread().getName() + " consumió " + coinsConsumidas + " | Restantes: " + coins.get());
            }, "Jugador-" + (i + 1));
        }

        //Iniciar cada hilo
        for (int i = 0; i<numeroJugadores; i++){
            threads[i].start();
        }

        //Terminar cada hilo
        for (int i = 0; i<numeroJugadores; i++){
            try {
                threads[i].join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        //Al final debe imprimirse el balance final de monedas 
        System.out.println("Monedas restantes: " + coins);
        //Cerar Scanner
        scanner.close();
    }
}
