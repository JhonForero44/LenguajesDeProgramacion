import java.util.ArrayList;
import java.util.List;

public class ProductoConsumidorOpcionalTres {
    public static void main(String[] args) {
        Buffer buffer = new Buffer(20);

        Runnable r1 = () -> {
            for (int i = 0; i < 20; i++) {
                buffer.productor("Hola");
            }
        };

        Runnable r2 = () -> {
            for (int i = 0; i < 20; i++) {
                buffer.consumidor();
            }
        };

        Thread thread1 = new Thread(r1);
        Thread thread2 = new Thread(r1);
        Thread thread3 = new Thread(r2);
        Thread thread4 = new Thread(r2);

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
            thread4.join();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("Programa finalizado.");
    }

}

class Buffer {
    private final int MAX_SIZE;
    private final List<String> lista = new ArrayList<>();
    private final Object lock = new Object();

    public Buffer(int maxSize) {
        this.MAX_SIZE = maxSize;
    }

    public void productor(String mensaje) {
        synchronized (lock) {
            while (lista.size() == MAX_SIZE) {
                System.out.println("Buffer lleno → productor espera...");
                try {
                    lock.wait();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }

            lista.add(mensaje);
            System.out.println("Productor agregó: " + mensaje + " | Tamaño buffer = " + lista.size());

            lock.notifyAll();
        }
    }

    public String consumidor() {
        synchronized (lock) {
            while (lista.isEmpty()) {
                System.out.println("Buffer vacío → consumidor espera...");
                try {
                    lock.wait();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }

            String msg = lista.remove(0);
            System.out.println("Consumidor retiró: " + msg + " | Tamaño buffer = " + lista.size());

            lock.notifyAll();

            return msg;
        }
    }

}