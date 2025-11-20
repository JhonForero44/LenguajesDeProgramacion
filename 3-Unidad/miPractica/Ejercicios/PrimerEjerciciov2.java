/*
Crea un programa en Java que:
Tenga dos hilos.
El Hilo 1 debe imprimir 5 veces el mensaje:
→ "Hola desde el hilo 1"
El Hilo 2 debe imprimir 5 veces el mensaje:
→ "Hola desde el hilo 2"
Entre cada impresión, cada hilo debe esperar 300 ms usando Thread.sleep().
*/
package Ejercicios;

import java.util.Scanner;

public class PrimerEjerciciov2 {
    public static void main(String[] args) {
        
        //Solicitar datos
        Scanner scanner = new Scanner(System.in);

        //Ingresa el numero de Hilos a crear
        System.out.printf("Ingresa el numero de Hilos a crear: ");
        int numeroHilos = scanner.nextInt();

        //Crear lista de hilos
        Thread[] thread = new Thread[numeroHilos];

        //Iniciarlizar cada Hilo
        for (int i = 0; i < numeroHilos; i++) {
            final int id = i + 1; // para que empiece desde 1

            thread[i] = new Thread(() -> {
                for (int j = 0; j < 5; j++) {
                    
                    System.out.println("Hola desde el hilo " + id);
                    try {
                        Thread.sleep(300);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
        }

        //Iniciar Hilos
        for (int i = 0; i<numeroHilos;i++){
            thread[i].start();
        }

        //Cerrar Hilos
        for (int i = 0; i<numeroHilos;i++){
            try {
                thread[i].join();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        //Cerar escaner
        scanner.close();

    }
}

