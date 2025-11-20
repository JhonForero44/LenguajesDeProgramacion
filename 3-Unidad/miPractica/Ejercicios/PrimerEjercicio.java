/*
Crea un programa en Java que:
Tenga dos hilos.
El Hilo 1 debe imprimir 5 veces el mensaje:
→ "Hola desde el hilo 1"
El Hilo 2 debe imprimir 5 veces el mensaje:
→ "Hola desde el hilo 2"
Entre cada impresión, cada hilo debe esperar 300 ms usando Thread.sleep().
*/
package Ejercicios;

public class PrimerEjercicio {
    
    static class Hilo1 extends Thread {
        public void run() {
            for (int i = 0; i<5;i++){
                System.out.printf("\nHola desde el hilo 1");
                try {
                    Thread.sleep(300);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }

    static class Hilo2 extends Thread {
        public void run() {
            for (int i = 0; i<5;i++){
                System.out.printf("\nHola desde el hilo 2");
                try {
                    Thread.sleep(300);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void main(String[] args) {

        // Crear los objetos de los hilos
        Hilo1 t1 = new Hilo1();
        Hilo2 t2 = new Hilo2();

        // Iniciar los hilos
        t1.start();
        t2.start();
    }
}
