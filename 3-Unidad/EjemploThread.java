/*
 Thread
 Es una clase en Java (es decir, un molde que puede tener propiedades y comportamientos).
 Cuando heredas de Thread, tu clase se convierte directamente en un hilo.
 */

class Jugador extends Thread {
    public void run() {
        System.out.println("⚽ El jugador corre hacia el balón");
    }
}

public class EjemploThread {
    public static void main(String[] args) {
        Jugador j1 = new Jugador();
        j1.start();
    }
}
