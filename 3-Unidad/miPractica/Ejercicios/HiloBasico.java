/*
Enunciado
Crea un programa en Java que lance 3 hilos.
Cada hilo debe imprimir su nombre 5 veces, con un pequeño tiempo de espera entre cada impresión.
El objetivo:
Entender cómo se ejecutan varios hilos “intercalados”.
*/

package Ejercicios;

public class HiloBasico {

    // Método que ejecutan todos los hilos
    public static void ejecutar() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Soy el hilo " + Thread.currentThread().getName() + " → iteración " + i);
            try {
                Thread.sleep(300);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {

        // Cantidad de Hilos
        int numeroHilo = 3;

        // Creamos el arreglo de Hilos
        Thread[] thread = new Thread[numeroHilo];

        // Creamos los 3 hilos
        Thread t1 = new Thread(() -> ejecutar(), "Hilo-1");
        Thread t2 = new Thread(() -> ejecutar(), "Hilo-2");
        Thread t3 = new Thread(() -> ejecutar(), "Hilo-3");

        // Asignamos los hilos al arreglo
        thread[0] = t1;
        thread[1] = t2;
        thread[2] = t3;

        // Iniciamos los hilos
        for (int i = 0; i < numeroHilo; i++) {
            thread[i].start();
        }

        // Finalizamos los hilos
        for (int i = 0; i < numeroHilo; i++) {
            try {
                thread[i].join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

    }
}
