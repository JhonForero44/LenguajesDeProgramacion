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

package ExplicacionJavaOracle;

//Libreria importar para usar Variaables Atomicas
import java.util.concurrent.atomic.AtomicInteger;

public class VariablesAtomicas {

    // Variable entera compartida para todos los hilos
    static AtomicInteger contador = new AtomicInteger(0);

    public static void main(String[] args) throws Exception {

        // Crear HILO1
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++)
                contador.incrementAndGet();

        });

        // Crear HILO2
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++)
                contador.incrementAndGet();
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(contador.get());
    }
}


/*
1. get()
Devuelve el valor actual.
int valor = contador.get();

2. set(int newValue)
Asigna un valor nuevo directamente (NO es operación compuesta, solo escritura atómica).
contador.set(10);

3. getAndSet(int newValue)
Devuelve el valor viejo y luego coloca el nuevo.
int viejo = contador.getAndSet(100);

4. incrementAndGet()
Incrementa en +1 y devuelve el nuevo valor.
int nuevo = contador.incrementAndGet();

5. getAndIncrement()
Devuelve el valor actual y luego incrementa.
int antes = contador.getAndIncrement();

6. decrementAndGet()
Decrementa en -1 y devuelve el nuevo valor.
contador.decrementAndGet();

7. getAndDecrement()
Devuelve el valor actual y luego decrementa.
contador.getAndDecrement();

8. addAndGet(int delta)
Suma un valor y devuelve el nuevo.
contador.addAndGet(5);  // suma 5

9. getAndAdd(int delta)
Devuelve el valor actual y luego suma.
contador.getAndAdd(3);

*/