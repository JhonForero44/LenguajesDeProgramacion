public class PartidoFutbol {

    // Método para mostrar qué hilo envía el mensaje
    static void hiloMensaje(String mensaje) {
        String nombreHilo = Thread.currentThread().getName();
        System.out.println("[" + nombreHilo + "] " + mensaje);
    }

    // Clase interna que representa al comentarista (segundo hilo)
    private static class Comentarista implements Runnable {
        @Override
        public void run() {
            // "Narración" del partido
            String[] jugadas = {
                "Comienza el partido en el estadio!",
                "El equipo local toca el balón con calma...",
                "Pase largo hacia el delantero...",
                "Disparo potente al arco!",
                "GOOOOOOL!!! 🎉",
                "El público enloquece!",
                "El árbitro pita el final del primer tiempo",
                "Comienza la segunda parte...",
                "Tiro de esquina peligroso...",
                "Final del partido, gran victoria local!"
            };

            // Recorremos las jugadas con pausas
            for (String jugada : jugadas) {
                try {
                    Thread.sleep(2000); // pausa de 2 segundos
                    hiloMensaje(jugada);
                } catch (InterruptedException e) {
                    hiloMensaje("¡La narración fue interrumpida!");
                    return; // salir del bucle si fue interrumpido
                }
            }
        }
    }

    // Hilo principal: el árbitro
    public static void main(String[] args) throws InterruptedException {
        long tiempoMaximo = 1000 * 20; // 20 segundos de tiempo máximo
        hiloMensaje("El árbitro entra al campo y se prepara para el inicio del partido.");

        // Registrar el tiempo de inicio
        long inicio = System.currentTimeMillis();

        // Crear y arrancar el hilo del comentarista
        Thread comentarista = new Thread(new Comentarista());
        comentarista.start();

        hiloMensaje("El árbitro da la orden: ¡Comienza el partido!");

        // Supervisar el hilo del comentarista (igual que en el ejemplo anterior)
        while (comentarista.isAlive()) {
            hiloMensaje("El árbitro observa el desarrollo del juego...");
            comentarista.join(1000); // espera 1 segundo

            long tiempoActual = System.currentTimeMillis();
            long transcurrido = tiempoActual - inicio;

            if (transcurrido > tiempoMaximo && comentarista.isAlive()) {
                hiloMensaje("El tiempo se agotó, ¡el árbitro pita el final!");
                comentarista.interrupt(); // interrumpe la narración
                comentarista.join();
            }
        }

        hiloMensaje("El árbitro abandona el campo. Partido finalizado.");
    }
}
