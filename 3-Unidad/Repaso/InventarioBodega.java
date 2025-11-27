/*
EJERCICIO: Inventario con múltiples hilos
*/

/*
    Crea al menos 4 hilos:
    2 hilos agregadores (producen)
    2 hilos retiradores (consumen)
    Al final, imprime el stock final para verificar si quedó en un valor lógico. 
     */

public class InventarioBodega {
    public static void main(String[] args) {

        Inventario inventario = new Inventario();

        Runnable r1 = () -> {
            for (int i = 0; i < 100; i++) {
                inventario.agregar(10);
            }
        };

        Runnable r2 = () -> {
            for (int i = 0; i < 100; i++) {
                inventario.agregar(30);
            }
        };

        Runnable r3 = () -> {
            for (int i = 0; i < 100; i++) {
                inventario.retirar(10);
            }
        };

        Runnable r4 = () -> {
            for (int i = 0; i < 100; i++) {
                inventario.retirar(20);
            }
        };

        Thread thread1 = new Thread(r1);
        Thread thread2 = new Thread(r2);
        Thread thread3 = new Thread(r3);
        Thread thread4 = new Thread(r4);

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

        inventario.getStock();
    }
}

/*
 * Tienes una clase Inventario que mantiene la cantidad de productos en una
 * bodega.
 * Debes implementar los métodos:
 * agregar(int cantidad)
 * retirar(int cantidad)
 * getStock() (solo lectura)
 * 
 * ✔️ Reglas del ejercicio
 * El stock no puede quedar negativo.
 * Si un hilo intenta retirar más de lo disponible, debe esperar hasta que haya
 * suficiente stock.
 * 
 * Múltiples hilos harán:
 * Unos agregarán productos continuamente.
 * Otros retirarán productos continuamente.
 * 
 * Usa un solo lock compartido para proteger las operaciones del stock.
 * Debes usar wait() y notifyAll() en los casos adecuados.
 * 
 */
class Inventario {

    private final Object lock = new Object();
    private int numeroProductos;

    public void agregar(int cantidad) {
        synchronized (lock) {
            numeroProductos += cantidad;
            lock.notifyAll();
        }        
    }

    public void retirar(int cantidad) {
        synchronized (lock) {

            // Mientras no haya suficientes productos → esperar
            while (numeroProductos < cantidad) {
                try {
                    lock.wait(); // Espera hasta que haya stock
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            numeroProductos -= cantidad; // Ahora sí puede retirar
            lock.notifyAll(); // Despierta a posibles agregadores o retiradores
        }
    }

    public void getStock() {
        System.out.printf("Stock final -> " + numeroProductos);
    }
}