public class HiloPaso1 implements Runnable {

    @Override
    public void run() {
        // Código que se ejecuta dentro del hilo secundario
        System.out.println("Hola desde el hilo: " + Thread.currentThread().getName());
    }

    public static void main(String[] args) {
        // Creamos el hilo usando nuestra clase que implementa Runnable
        Thread miHilo = new Thread(new HiloPaso1());

        // Iniciamos el hilo: Java llamará a run() en paralelo
        miHilo.start();

        // Esto lo imprime el hilo principal (main)
        System.out.println("Esto lo imprime el hilo principal: " + Thread.currentThread().getName());
    }
}
