package PrimeraTarea;
import java.util.Scanner;
//Libreria importar para usar Variaables Atomicas
import java.util.concurrent.atomic.AtomicInteger;

public class GameManagerVariableAtomica {
    //Variable entera compartida para todos los hilos
    static AtomicInteger coins = new AtomicInteger(10000);

    public static void main(String[] args) {
        
        //Pedir numero de jugadores 
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Ingresa el numero de jugadores: ");
        int numeroJugadores = scanner.nextInt();

        //Iniciar los hilo para cada jugador 
        Thread[] threads = new Thread[numeroJugadores];

        //Cada hilo consume una cantidad de monedas 
        for (int i = 0; i < numeroJugadores; i++) {

            int coinsConsumidas = (int) (Math.random() * 100) + 1;

            threads[i] = new Thread(() -> {
                // Consumir monedas de forma atómica
                coins.getAndAdd(-coinsConsumidas);
                System.out.println(
                    Thread.currentThread().getName() +
                    " consumió " + coinsConsumidas +
                    " | Restantes: " + coins.get()
                );
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
                // TODO: handle exception
            }
        }

        //Al final debe imprimirse el balance final de monedas 
        System.out.println("Monedas restantes: " + coins);
        //Cerar Scanner
        scanner.close();
    }
}
