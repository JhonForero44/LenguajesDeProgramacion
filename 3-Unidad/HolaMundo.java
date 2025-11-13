public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola mundo!");
    }
}

/* Tipos de datos
int edad = 25;
double altura = 1.75;
char letra = 'A';
boolean activo = true;
String nombre = "Jhon";
*/

/* 
 Condicionales:
if (edad >= 18) {
    System.out.println("Eres mayor de edad");
} else {
    System.out.println("Eres menor de edad");
}
*/

/* 
Bucle For
for (int i = 0; i < 5; i++) {
    System.out.println("Número: " + i);
}
*/

/* 
Bucle While
int i = 0;
while (i < 5) {
    System.out.println("i = " + i);
    i++;
}
*/

/* 
Metodos
public static int sumar(int a, int b) {
    return a + b;
}

public static void main(String[] args) {
    int resultado = sumar(5, 3);
    System.out.println("La suma es: " + resultado);
}
*/

/* 
POO Basico
// Definición de la clase
public class Persona {
    String nombre;
    int edad;

    // Constructor
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Método
    public void saludar() {
        System.out.println("Hola, mi nombre es " + nombre + " y tengo " + edad + " años.");
    }
}

// Clase principal
public class Main {
    public static void main(String[] args) {
        Persona p1 = new Persona("Jhon", 25);
        p1.saludar();
    }
}
*/

/* 
Principios de la POO

Encapsulamiento
public class Cuenta {
    private double saldo;
    public void depositar(double monto) { saldo += monto; }
    public double getSaldo() { return saldo; }
}

Herencia
public class Animal {
    void comer() { System.out.println("Comiendo..."); }
}

public class Perro extends Animal {
    void ladrar() { System.out.println("Guau!"); }
}

// Uso
Perro p = new Perro();
p.comer();  // Heredado
p.ladrar(); // Propio

*/

