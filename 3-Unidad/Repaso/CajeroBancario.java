/*
Ejercicio: Cajero Bancario (versión corta)
Crea una clase llamada CuentaBancaria con:
un atributo saldo
un Object lock = new Object();
Debes implementar estos métodos:
1. depositar(int cantidad)
Suma la cantidad al saldo.
Usa synchronized(lock).
Llama a notifyAll().
2. retirar(int cantidad)
Usa synchronized(lock).
Si cantidad > saldo, el hilo debe esperar con wait().
Cuando haya suficiente saldo, hace el retiro.
3. getSaldo()
Solo lectura.

🧵 Parte del Main (lo que debes hacer)
Crea:
2 hilos que depositan 100 veces cantidades pequeñas.
2 hilos que retiran 100 veces cantidades pequeñas.
Al final:
Imprime el saldo final.

🎯 Objetivo del ejercicio
Practicar intrinsic locks (synchronized(lock)).
Usar adecuadamente wait() y notifyAll().
Manejar correctamente la lógica:
Los retiradores NO deben dejar saldo negativo.
Los retiradores deben esperar si no hay suficiente dinero.
Los depositadores deben despertar a los retiradores.
*/

public class CajeroBancario {
    public static void main(String[] args) {
        CuentaBancaria cuentabancaria = new CuentaBancaria();

        Runnable r1 = () -> {
            for (int i = 0; i < 100; i++) {
                cuentabancaria.depositar(10);
            }
        };

        Runnable r2 = () -> {
            for (int i = 0; i < 100; i++) {
                cuentabancaria.depositar(10);
            }
        };

        Runnable r3 = () -> {
            for (int i = 0; i < 100; i++) {
                cuentabancaria.retirar(10);
            }
        };

        Runnable r4 = () -> {
            for (int i = 0; i < 100; i++) {
                cuentabancaria.retirar(10);
            }
        };

        Thread thread1 = new Thread(r1);
        Thread thread2 = new Thread(r2);
        Thread thread3 = new Thread(r3);
        Thread thread4 = new Thread(r4);

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
            thread4.join();
        } catch (Exception e) {
            e.printStackTrace();
        }

        cuentabancaria.getSaldo();
    }
}

class CuentaBancaria {
    private int saldo;
    private Object lock = new Object();

    public void depositar(int cantidad) {
        synchronized (lock) {
            saldo += cantidad;
            lock.notifyAll();
        }
    }

    public void retirar(int cantidad) {
        synchronized (lock) {
            // Esperar mientras no haya suficiente saldo
            while (cantidad > saldo) {
                try {
                    lock.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            // Ya hay saldo, ahora retirar
            saldo -= cantidad;
            lock.notifyAll();
        }
    }

    public void getSaldo() {
        System.out.printf("El saldo final es de: " + saldo);
    }
}