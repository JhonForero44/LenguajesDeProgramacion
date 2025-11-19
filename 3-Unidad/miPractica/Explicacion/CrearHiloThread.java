package Explicacion;

class HiloThread extends Thread {
    public void run() {
    System.out.println("Hola desde el hilo: " + Thread.currentThread().getName());
    }
}

public class CrearHiloThread {
    public static void main(String[] args) {
    HiloThread hilo1 = new HiloThread();    
    hilo1.start(); // IMPORTANTE: usar start(), NO run()
}
}
