class Buffer {
    private int inventario;
    private final int capacidad;
    private boolean cerrado = false;

    public Buffer(int inventarioInicial, int capacidad) {
        this.inventario = inventarioInicial;
        this.capacidad = capacidad;
    }

    // Llamado al final del programa
    public synchronized void cerrar() {
        cerrado = true;
        notifyAll(); // despierta a hilos esperando
    }

    public synchronized void producir(int cantidad) throws InterruptedException {
        while (inventario + cantidad > capacidad && !cerrado) {
            System.out.println(Thread.currentThread().getName() + " espera — buffer lleno");
            wait();
        }

        if (cerrado) return; // salir si el sistema ya cerró

        inventario += cantidad;
        System.out.println(Thread.currentThread().getName() +
                " produjo → inventario = " + inventario);

        notifyAll();
    }

    public synchronized void consumir(int cantidad) throws InterruptedException {
        while (inventario - cantidad < 0 && !cerrado) {
            System.out.println(Thread.currentThread().getName() + " espera — inventario = 0");
            wait();
        }

        if (cerrado) return; // salir si el sistema ya cerró

        inventario -= cantidad;
        System.out.println(Thread.currentThread().getName() +
                " consumió → inventario = " + inventario);

        notifyAll();
    }

    public synchronized int getInventario() {
        return inventario;
    }
}

class Productor extends Thread {
    private final Buffer buffer;

    public Productor(Buffer buffer, String nombre) {
        super(nombre);
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 5; i++) {
                buffer.producir(1);
                sleep(300);
            }
        } catch (InterruptedException e) {}
    }
}

class Consumidor extends Thread {
    private final Buffer buffer;

    public Consumidor(Buffer buffer, String nombre) {
        super(nombre);
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 5; i++) {
                buffer.consumir(1);
                sleep(350);
            }
        } catch (InterruptedException e) {}
    }
}

public class ProductorConsumidorLimite {
    public static void main(String[] args) {
        Buffer buffer = new Buffer(3, 5);

        Thread p1 = new Productor(buffer, "Productor-1");
        Thread p2 = new Productor(buffer, "Productor-2");
        Thread c1 = new Consumidor(buffer, "Consumidor-1");
        Thread c2 = new Consumidor(buffer, "Consumidor-2");

        p1.start();
        p2.start();
        c1.start();
        c2.start();

        try {
            p1.join();
            p2.join();
            c1.join();
            c2.join();
        } catch (Exception e) {}

        buffer.cerrar(); // Despierta a hilos que estén esperando

        System.out.println("Inventario final = " + buffer.getInventario());
        System.out.println("Programa terminado sin bloqueos.");
    }
}
