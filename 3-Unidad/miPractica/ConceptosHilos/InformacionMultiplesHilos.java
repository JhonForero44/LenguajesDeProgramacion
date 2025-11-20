package ConceptosHilos;

import java.util.Scanner;

public class InformacionMultiplesHilos {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("¿Cuántos hilos quieres crear?: ");
        int n = scanner.nextInt();

        Thread[] hilos = new Thread[n];

        for (int i = 0; i < n; i++) {

            final int idHilo = i + 1;

            hilos[i] = new Thread(() -> {

                Thread t = Thread.currentThread(); // hilo actual
                t.setName("Hilo-" + idHilo);

                for (int j = 0; j < 5; j++) {

                    System.out.println("----- Iteración " + (j + 1) + " -----");
                    System.out.println("Nombre del hilo: " + t.getName());
                    //System.out.println("ID del hilo: " + t.getId());
                    System.out.println("Clase: " + t.getClass().getName());
                    System.out.println("Prioridad: " + t.getPriority());
                    System.out.println("Estado: " + t.getState());
                    System.out.println("-------------------------\n");

                    try {
                        Thread.sleep(300);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
        }

        // Iniciar los hilos
        for (int i = 0; i < n; i++) {
            hilos[i].start();
        }

        scanner.close();
    }
}
