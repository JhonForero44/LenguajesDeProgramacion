/*
Ejercicio: Simulación de cajeros en un banco
Descripción:
Imagina un banco con varios cajeros automáticos. Cada cajero atiende a un cliente diferente,
pero todos usan la misma cuenta bancaria compartida para consultar el saldo.
Lo que debes hacer:
- Crea una clase que represente una cuenta con un saldo inicial.
- Crea varios hilos, cada uno simulando un cajero automático.
- Cada cajero debe intentar retirar una cantidad pequeña varias veces.
- Solo uno a la vez debe poder modificar el saldo real para evitar inconsistencias.
- Cuando todos los hilos terminen, muestra el saldo final.
*/

public class CajerosAutomaticos {
    public static void main(String[] args) {
        Cunete cunete = new Cunete();

        Runnable r1 = () -> {
            for (int i = 0; i<5; i++){
                cunete.retirar(50);
            }
        };

        Runnable r2 = () -> {
            for (int i = 0; i<5; i++){
                cunete.retirar(50);
            }
        };

        Runnable r3 = () -> {
            for (int i = 0; i<5; i++){
                cunete.retirar(50);
            }
        };

        Thread thread1 = new Thread(r1);
        Thread thread2 = new Thread(r2);
        Thread thread3 = new Thread(r3);

        thread1.start();
        thread2.start();
        thread3.start();

        cunete.getSaldo();
    }
}

class Cunete{
    private int saldoInicial = 10000;
    Object lock = new Object();

    public void retirar(int valorRetirar){
        synchronized (lock){
            saldoInicial -= valorRetirar;
        }
    }

    public void getSaldo(){
        System.out.printf("El saldo final es de: " + saldoInicial);
    }
}