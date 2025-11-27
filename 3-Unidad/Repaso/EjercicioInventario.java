
public class EjercicioInventario {

    /*
     * 
     * En la clase Main:
     * - Crea un solo objeto Inventario.
     * - Crea 3 hilos:
     * - Un hilo que llama varias veces a agregar.
     * - Dos hilos que intentan llamar varias veces a retirar.
     * - Ejecuta el programa y observa los resultados:
     * - La operación sincronizada debe funcionar correctamente.
     * - La operación NO sincronizada debería mostrar comportamiento incorrecto
     * (cantidad negativa, saltos extraños, etc.).
     * 
     */

    public static void main(String[] args) {
        Inventario inventario = new Inventario();

        Runnable r1 = () -> {
            for (int i = 0; i < 1000000; i++) {
                inventario.agregar(1);
            }
        };

        Runnable r2 = () -> {
            for (int i = 0; i < 1000000; i++) {
                inventario.retirar(1);
            }
        };

        Thread thread1 = new Thread(r1);
        Thread thread2 = new Thread(r2);
        Thread thread3 = new Thread(r2);

        thread1.start();
        thread2.start();
        thread3.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.print("La cantidad final es: " + inventario.getCantidad());
    }

}

class Inventario {
    /*
     * 
     * Crea un programa en Java con las siguientes condiciones:
     * Una clase llamada Inventario. Esta clase debe tener:
     * - Una variable entera llamada cantidad.
     * - Un objeto de bloqueo: private final Object lockA = new Object();
     * La clase debe tener dos métodos:
     * - agregar(int n)
     * - retirar(int n)
     * Ambas operaciones deben modificar cantidad, pero:
     * Solo una de las operaciones debe estar sincronizada usando
     * synchronized(lockA), tú eliges cuál.
     * La otra operación NO debe estar sincronizada para que tú puedas observar
     * problemas de concurrencia si la llamas desde varios hilos.
     * 
     * 
     */
    private final Object lock = new Object();
    private int cantidad;

    public void agregar(int n) {
        synchronized (lock) {
            cantidad = cantidad + n;
        }
    }

    public void retirar(int n) {
        //synchronized (lock) {
            cantidad = cantidad - n;
        //}
    }

    public int getCantidad() {
        return cantidad;
    }

}