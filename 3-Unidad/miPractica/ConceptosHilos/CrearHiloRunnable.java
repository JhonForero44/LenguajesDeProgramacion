package ConceptosHilos;

class HiloRunnable implements Runnable {
    public void run() {
        System.out.println("Ejecutando tarea en: " + Thread.currentThread().getName());
    }
}

public class CrearHiloRunnable {
    public static void main(String[] args) {
        Thread hilo = new Thread(new HiloRunnable());
        hilo.start();
    }
}