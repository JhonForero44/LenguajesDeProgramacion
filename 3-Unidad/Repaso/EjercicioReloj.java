/*
Descripción:
Crea un programa en Java donde un hilo funcione como un reloj que imprime la hora cada segundo.
Mientras tanto, el hilo principal sigue ejecutando otra tarea (por ejemplo, imprimir un mensaje cada 3 segundos).
*/
import java.time.LocalTime;

public class EjercicioReloj {
    public static void main(String[] args) {
        Thread reloj = new Thread(new Reloj());
        reloj.start();

        // Hilo principal
        for (int i = 0; i < 5; i++) {
            System.out.println("Hilo principal trabajando...");
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class Reloj implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            LocalTime hora = LocalTime.now();
            System.out.println("Hora actual: " + hora);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
