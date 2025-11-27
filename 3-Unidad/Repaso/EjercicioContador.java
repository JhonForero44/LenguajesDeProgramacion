/*
Descripción:
Vas a crear un programa donde varios hilos incrementen el mismo contador.
El contador está en un objeto compartido, así que debes usar synchronized para evitar que dos hilos lo modifiquen al mismo tiempo.
*/

/*
📝 Requisitos del ejercicio:
1. Crea una clase llamada, por ejemplo, Contador, que tenga:
* Una variable entera valor
* Un método incrementar() que aumente el valor en 1
→ Este método debe estar sincronizado usando synchronized.

2. Crea una clase HiloIncrementador que implemente Runnable.
Cada hilo debe:
* Recibir el contador compartido
* Incrementarlo, por ejemplo, 1000 veces

3. En el main:
* Crea un objeto Contador
* Crea y arranca 5 hilos HiloIncrementador
* Espera a que todos terminen (join)
* Muestra el valor final del contador

El resultado correcto debe ser 5000 (5 hilos × 1000 incrementos).
Sin synchronized, el resultado sería menor por condiciones de carrera.

*/


public class EjercicioContador {
    public static void main(String[] args) {
        Contador contador = new Contador();
        Thread thread1 = new Thread(new HiloIncrementador(contador));
        Thread thread2 = new Thread(new HiloIncrementador(contador));
        Thread thread3 = new Thread(new HiloIncrementador(contador));
        Thread thread4 = new Thread(new HiloIncrementador(contador));
        Thread thread5 = new Thread(new HiloIncrementador(contador));

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();
        thread5.start();

        try {
            thread1.join();
            thread2.join();    
            thread3.join();
            thread4.join();    
            thread5.join();
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        System.out.println("El resultado final del contador es: " + contador.valorContador());
    }
}

class HiloIncrementador implements Runnable{
    private Contador contador;

    public HiloIncrementador(Contador contador) {
        this.contador = contador;    // Se recibe desde afuera
    }

    @Override    
    public void run(){
        for (int i = 0; i<1000;i++){
            contador.incrementar();
        }
    }
}

class Contador{

    private int contador = 0;

    public synchronized void incrementar(){
        contador ++;
    }

    public int valorContador(){
        return contador;
    }    
}