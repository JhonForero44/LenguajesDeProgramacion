package ConceptosHilos;

public class CreacionVariosHilos {
    
    public static void main(String[] args) {
        for(int i = 1; i <= 5; i++){
        Thread hilo = new Thread(() ->System.out.println("Hilo ejecutándose: " + Thread.currentThread().getName()));
        hilo.start();
        }
    }
}