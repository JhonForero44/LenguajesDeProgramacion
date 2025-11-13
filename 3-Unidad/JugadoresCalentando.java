// Simulación simple con hilos en Java
public class JugadoresCalentando {

    // Clase interna que representa a cada jugador (tarea que va en un hilo)
    static class Jugador implements Runnable {
        private String nombre;

        // Constructor
        public Jugador(String nombre) {
            this.nombre = nombre;
        }

        // Este método es lo que el hilo va a ejecutar
        @Override
        public void run() {
            for (int i = 1; i <= 5; i++) {
                System.out.println(nombre + " está haciendo ejercicio " + i);
                try {
                    Thread.sleep(1000); // pausa de 1 segundo entre ejercicios
                } catch (InterruptedException e) {
                    System.out.println(nombre + " fue interrumpido.");
                }
            }
            System.out.println(nombre + " ha terminado su calentamiento 🏁");
        }
    }

    // Método principal
    public static void main(String[] args) {
        // Creamos 3 jugadores (3 tareas)
        Thread j1 = new Thread(new Jugador("Jugador 1"));
        Thread j2 = new Thread(new Jugador("Jugador 2"));
        Thread j3 = new Thread(new Jugador("Jugador 3"));

        System.out.println("🔔 Comienza el calentamiento...");

        // Iniciamos los tres hilos
        j1.start();
        j2.start();
        j3.start();

        // Mensaje final cuando todos terminan
        System.out.println("🏟️ Todos los jugadores están calentando al mismo tiempo...");
    }
}
