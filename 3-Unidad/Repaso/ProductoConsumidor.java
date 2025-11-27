/*
🧪 Ejercicio: Productor–Consumidor con Buffer (sin usar BlockingQueue)
Este ejercicio es excelente para practicar:
- wait()
- notify()
- sincronización fina con objetos compartidos
- control de concurrencia en un buffer limitado

📝 Descripción del ejercicio
Vas a simular que:
- Un Productor genera números (0,1,2,3,...)
- Un Consumidor los toma del buffer y los “procesa”
- Ambos trabajan con un buffer compartido, de tamaño limitado (por ejemplo, 5 posiciones)

Cuando:
- El buffer está lleno, el Productor debe detenerse (wait)
- El buffer está vacío, el Consumidor debe detenerse (wait)
Cuando uno agrega o quita un elemento, debe despertar al otro hilo usando notify().


*/

import java.util.ArrayList;
import java.util.List;

public class ProductoConsumidor {
    public static void main(String[] args) {

        Buffer buffer = new Buffer();

        Thread t1 = new Thread(new Productor(buffer));
        Thread t2 = new Thread(new Consumidor(buffer));

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Proceso terminado.");
    }
}

class Buffer {

    private final int MAX_SIZE = 5;
    private final List<Integer> cola = new ArrayList<>();

    public synchronized void producir(int valor) throws InterruptedException {
        // Si el buffer está lleno → esperar
        while (cola.size() == MAX_SIZE) {
            System.out.println("Buffer lleno → productor espera...");
            wait();
        }

        cola.add(valor);
        System.out.println("Producido: " + valor);

        // Avisar al consumidor que ya hay un elemento
        notify();
    }

    public synchronized int consumir() throws InterruptedException {
        // Si el buffer está vacío → esperar
        while (cola.isEmpty()) {
            System.out.println("Buffer vacío → consumidor espera...");
            wait();
        }

        int valor = cola.remove(0); // Consumir el primero de la lista
        System.out.println("Consumido: " + valor);

        // Avisar al productor que hay espacio disponible
        notify();

        return valor;
    }
}

class Productor implements Runnable {

    private Buffer buffer;

    public Productor(Buffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 15; i++) {
                buffer.producir(i);
                Thread.sleep(300); // opcional
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}


class Consumidor implements Runnable {

    private Buffer buffer;

    public Consumidor(Buffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 15; i++) {
                buffer.consumir();
                Thread.sleep(500); // opcional
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
