package Explicacion;

class CrearHiloRunnable implements Runnable{
    public void run() {
    System.out.println("Ejecutando tarea en: " + Thread.currentThread().getName());
    }    
}

public class Main {
    public static void main(String[] args) {
    Thread hilo = new Thread(new CrearHiloRunnable());
    hilo.start();
}
}