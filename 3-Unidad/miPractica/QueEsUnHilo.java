/*
Un hilo es una unidad de ejecución independiente dentro de un programa.
Un programa puede ejecutar varias tareas al mismo tiempo, cada una en su propio
hilo.

Para que sirve:
- Ejecutar tareas en paralelo.
- Mejorar rendimiento en programas con muchas tareas.
- No bloquear todo el programa por una operación lenta.

*/

public class QueEsUnHilo {
    
    public static void main(String[] args) {
        // ==== Hilo 1 ====
        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Hilo 1: mensaje " + i);
            }
        });

        // ==== Hilo 2 ====
        Thread thread2 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Hilo 2: mensaje " + i);
            }
        });

        //Iniciar los hilos
        thread1.start();
        thread2.start();
        
        System.out.println("Hilos iniciados. El main sigue...");

    }
}