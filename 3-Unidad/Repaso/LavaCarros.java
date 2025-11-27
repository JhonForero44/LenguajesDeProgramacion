class CarWash {

    private boolean ocupado = false; 
    private final Object lock = new Object();

    public void entrarALavar(String nombreCarro) throws InterruptedException {
        synchronized (lock) {
            System.out.println(nombreCarro + " quiere lavar...");

            while (ocupado) {
                System.out.println(nombreCarro + " espera... estación ocupada.");
                lock.wait();
            }

            ocupado = true;
            System.out.println(nombreCarro + " entra al lavado.");
        }
    }

    public void salirDelLavado(String nombreCarro) {
        synchronized (lock) {
            System.out.println(nombreCarro + " sale del lavado.");
            ocupado = false;

            lock.notifyAll(); // despertar a todos los carros esperando
        }
    }
}

public class LavaCarros {
    public static void main(String[] args) {

        CarWash carWash = new CarWash();

        Runnable carro = ( ) -> {
            String nombre = Thread.currentThread().getName();
            try {
                carWash.entrarALavar(nombre);
                Thread.sleep(1000); // simulando el lavado
                carWash.salirDelLavado(nombre);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        };

        Thread carro1 = new Thread(carro, "Carro A");
        Thread carro2 = new Thread(carro, "Carro B");
        Thread carro3 = new Thread(carro, "Carro C");

        carro1.start();
        carro2.start();
        carro3.start();
    }
}
