package ConceptosHilos;

public class InformacionDeHilo {

    public static void main(String[] args) {

        Thread hilo = new Thread(() -> {
            for (int i = 0; i < 5; i++) {

                Thread t = Thread.currentThread(); // obtener el hilo actual

                System.out.println("Iteración " + i);
                System.out.println("Nombre del hilo: " + t.getName());
                // System.out.println("ID del hilo: " + t.getId());
                System.out.println("Clase del hilo: " + t.getClass().getName());
                System.out.println("Prioridad: " + t.getPriority());
                System.out.println("Estado: " + t.getState());
                System.out.println("--------------------------------");

                try {
                    Thread.sleep(300);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        // puedes modificar el nombre si quieres
        hilo.setName("MiPrimerHilo");

        hilo.start();
    }
}
