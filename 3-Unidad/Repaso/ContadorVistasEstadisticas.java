public class ContadorVistasEstadisticas {
    public static void main(String[] args) {

        ContadorVisitas contadorVisitas = new ContadorVisitas();

        // Tres hilos que registran visitas
        Runnable registrar = () -> {
            for (int i = 0; i < 100; i++) {
                contadorVisitas.registrarVisita();
            }
        };

        // Un hilo que reinicia las visitas del día
        Runnable reiniciar = () -> {
            contadorVisitas.reiniciarDia();
        };

        Thread t1 = new Thread(registrar);
        Thread t2 = new Thread(registrar);
        Thread t3 = new Thread(registrar);
        Thread t4 = new Thread(reiniciar);

        t1.start();
        t2.start();
        t3.start();

        try {
            t1.join();
            t2.join();
            t3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        t4.start();

        try {
            t4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Mostrar resultados finales
        contadorVisitas.getTotales();
        contadorVisitas.getHoy();
    }
}

class ContadorVisitas {
    private int visitasTotales = 0;
    private int visitasHoy = 0;

    private final Object lockVisitas = new Object();
    private final Object lockHoy = new Object();

    public void registrarVisita() {
        synchronized (lockVisitas) {
            visitasTotales++;
        }

        synchronized (lockHoy) {
            visitasHoy++;
        }
    }

    public void reiniciarDia() {
        synchronized (lockHoy) {
            visitasHoy = 0;
        }
    }

    public synchronized void getTotales() {
        System.out.println("Visitas totales: " + visitasTotales);
    }

    public synchronized void getHoy() {
        System.out.println("Visitas hoy: " + visitasHoy);
    }
}
