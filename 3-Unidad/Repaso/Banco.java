/*
Descripción:
Vas a simular varios hilos intentando retirar dinero del mismo banco o cuenta.

Cada hilo representa un usuario intentando hacer retiros al mismo tiempo.
Necesitas usar synchronized para evitar que dos hilos retiren dinero simultáneamente y provoquen un saldo negativo.
*/


public class Banco {
    public static void main(String[] args) {
        CuentaBancaria cuenta = new CuentaBancaria(200000); // saldo inicial

        Thread c1 = new Thread(new Cliente(cuenta));
        Thread c2 = new Thread(new Cliente(cuenta));
        Thread c3 = new Thread(new Cliente(cuenta));

        c1.start();
        c2.start();
        c3.start();

        try {
            c1.join();
            c2.join();
            c3.join();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("Saldo final: " + cuenta.getSaldo());        
    }
}

class CuentaBancaria{
    private int saldo;

    public CuentaBancaria(int saldoInicial) {
        this.saldo = saldoInicial;
    }

    public synchronized void retirar(int monto){
        if (monto <= saldo) {
            saldo -= monto;
            System.out.println("Retiro exitoso de " + monto + ". Saldo restante: " + saldo);
        } else {
            System.out.println("Fondos insuficientes para el retiro de " + monto);
        }
    }

    public int getSaldo() {
        return saldo;
    }
}

class Cliente implements Runnable {

    private CuentaBancaria cuenta;

    public Cliente(CuentaBancaria cuenta) {
        this.cuenta = cuenta;
    }

    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {    // 5 retiros
            cuenta.retirar(50);         // monto a retirar
        }
    }
}
