package ConceptosHilos;

public class PausarHilo {

    public static void main(String[] args) {
        Thread hilo = new Thread(() -> {
            try {
                System.out.println("Hilo iniciando...");
                Thread.sleep(2000); // 2 segundos
                System.out.println("Hilo despertó!");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        hilo.start();
    }
}
