public class ProductoConsumidorOpcionUno {
    public static void main(String[] args) {

        Buffer buffer = new Buffer(1); // inventario máximo N = 10

        Productor p1 = new Productor(buffer, "Productor-1");
        Productor p2 = new Productor(buffer, "Productor-2");

        Consumidor c1 = new Consumidor(buffer, "Consumidor-1");
        Consumidor c2 = new Consumidor(buffer, "Consumidor-2");

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
    }
}

class Buffer {
    private final int MAX_SIZE;
    private int inventario = 0;

    public Buffer(int max) {
        this.MAX_SIZE = max;
    }

    public synchronized void producir(int cantidad) throws InterruptedException {
        // Si producir se pasa del tamaño → esperar
        while (inventario + cantidad > MAX_SIZE) {
            System.out
                    .println(Thread.currentThread().getName() + " espera — inventario lleno (" + inventario + ")");
            wait();
        }

        inventario += cantidad;
        System.out.println(
                Thread.currentThread().getName() + " produjo " + cantidad + " → inventario = " + inventario);
        notifyAll(); // despertar consumidores
    }

    public synchronized void consumir(int cantidad) throws InterruptedException {
        // Si no hay suficiente inventario → esperar
        while (inventario - cantidad < 0) {
            System.out
                    .println(Thread.currentThread().getName() + " espera — inventario vacío (" + inventario + ")");
            wait();
        }

        inventario -= cantidad;
        System.out.println(
                Thread.currentThread().getName() + " consumió " + cantidad + " → inventario = " + inventario);
        notifyAll(); // despertar productores
    }
}

class Productor extends Thread {
    private final Buffer buffer;

    public Productor(Buffer b, String nombre) {
        super(nombre);
        this.buffer = b;
    }

    @Override
    public void run() {
        try {
            while (true) {
                buffer.producir(1);
                sleep(500);
            }
        } catch (InterruptedException e) {
        }
    }
}

class Consumidor extends Thread {
    private final Buffer buffer;

    public Consumidor(Buffer b, String nombre) {
        super(nombre);
        this.buffer = b;
    }

    @Override
    public void run() {
        try {
            while (true) {
                buffer.consumir(1);
                sleep(600);
            }
        } catch (InterruptedException e) {
        }
    }
}
