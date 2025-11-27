class Buffer {
    private int valor;
    private boolean disponible = false; // indica si hay un valor listo
    private final Object lock = new Object();

    public void producir(int nuevoValor) throws InterruptedException {
        synchronized (lock) {
            while (disponible) { // si ya hay un valor, esperar
                System.out.println("Productor espera... buffer lleno");
                lock.wait();
            }

            valor = nuevoValor;
            System.out.println("Productor produce: " + valor);
            disponible = true;

            lock.notifyAll(); // despertar al consumidor
        }
    }

    public int consumir() throws InterruptedException {
        synchronized (lock) {
            while (!disponible) { // si no hay valor, esperar
                System.out.println("Consumidor espera... buffer vacío");
                lock.wait();
            }

            System.out.println("Consumidor consume: " + valor);
            disponible = false;

            lock.notifyAll(); // despertar al productor
            return valor;
        }
    }
}

public class Main {
    public static void main(String[] args) {

        Buffer buffer = new Buffer();

        Thread productor = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                try {
                    buffer.producir(i);
                    Thread.sleep(500); // pausa para ver la secuencia
                } catch (InterruptedException e) {
                }
            }
        });

        Thread consumidor = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                try {
                    buffer.consumir();
                    Thread.sleep(800); // pausa para ver la secuencia
                } catch (InterruptedException e) {
                }
            }
        });

        productor.start();
        consumidor.start();

        try {
            //productor.join();
            //consumidor.join();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
