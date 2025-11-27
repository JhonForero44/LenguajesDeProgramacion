
class Buffer {
    private int inventario;

    public Buffer(int inventarioInicial) {
        this.inventario = inventarioInicial;
    }

    public synchronized void producir(int cantidad) throws InterruptedException {
        inventario += cantidad;
        System.out.println(Thread.currentThread().getName() +
                " produjo " + cantidad + " → inventario = " + inventario);
        notifyAll();
    }

    public synchronized void consumir(int cantidad) throws InterruptedException {
        while (inventario - cantidad < 0) {
            System.out.println(Thread.currentThread().getName() +
                    " espera — inventario = 0");
            wait();
        }

        inventario -= cantidad;
        System.out.println(Thread.currentThread().getName() +
                " consumió " + cantidad + " → inventario = " + inventario);
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
            // Se repite exactamente 5 veces
            for (int i = 0; i < 5; i++) {
                buffer.producir(2);
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
            // Se repite exactamente 5 veces
            for (int i = 0; i < 5; i++) {
                buffer.consumir(2);
                sleep(400);
            }
        } catch (InterruptedException e) {}
    }
}

public class ProductoConsumidorOpcionalDos {
    public static void main(String[] args) {
        Buffer buffer = new Buffer(3); // inventario inicial mayor a 0

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
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("Inventario final = " + buffer.getInventario());

    }
}
