/*
Las variables atómicas pertenecen al paquete:
import java.util.concurrent.atomic.*;

Fueron creadas para resolver un problema muy específico:
Incrementar, decrementar o actualizar variables de manera segura en entornos
con múltiples hilos SIN usar synchronized y SIN usar locks.
Son muy rápidas, porque usan instrucciones atómicas del procesador (CAS: Compare And Swap).

¿Qué es una operación atómica? Una operación atómica significa que:
•No puede ser interrumpida,
•No puede ser dividida,
•Es 100% segura entre hilos sin candados
*/

package Explicacion;
//Libreria importar para usar Variaables Atomicas
import java.util.concurrent.atomic.AtomicInteger;

public class VariablesAtomicas {

    //Variable entera compartida para todos los hilos
    static AtomicInteger contador = new AtomicInteger(0);

    public static void main(String[] args) throws Exception {

        //Crear HILO1
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) contador.incrementAndGet();

        });

        //Crear HILO2
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) contador.incrementAndGet();
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(contador.get()); 
    }
}
