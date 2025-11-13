/*
 Runnable
 Es una interfaz, no una clase.
 Solo define qué tarea se va a ejecutar, pero no es el hilo en sí.
 Necesitas pasarla a un objeto Thread para que se ejecute.
 */

class Jugador implements Runnable {
    public void run() {
        System.out.println("⚽ El jugador corre hacia el balón");
    }
}

public class EjemploRunnable {
    public static void main(String[] args) {
        Thread hiloJugador = new Thread(new Jugador());
        hiloJugador.start();
    }
}
