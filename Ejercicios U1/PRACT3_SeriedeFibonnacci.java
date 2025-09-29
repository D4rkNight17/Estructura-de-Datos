//Iterativo

import java.math.BigInteger;

public class PRACT3_SeriedeFibonnacci{
    public static void main(String[] args) {
        int n = 10000; // cantidad de números de Fibonacci
        BigInteger[] serie = new BigInteger[n];

        long inicio = System.currentTimeMillis();

        // Primeros valores de la serie
        serie[0] = BigInteger.ZERO;
        serie[1] = BigInteger.ONE;

        // Calcular serie de Fibonacci hasta n
        for (int i = 2; i < n; i++) {
            serie[i] = serie[i - 1].add(serie[i - 2]);
        }

        long fin = System.currentTimeMillis();

        System.out.println("Se generaron " + n + " números de Fibonacci");
        System.out.println("⏱ Tiempo: " + (fin - inicio) + " ms");

        // Imprimir los primeros 20 como ejemplo
        System.out.println("\nPrimeros 20 números:");
        for (int i = 0; i < 20; i++) {
            System.out.println("F(" + i + ") = " + serie[i]);
        }

        // Último número (el número n de Fibonacci)
        BigInteger ultimo = serie[n - 1];
        System.out.println("\nNúmero " + n + " de Fibonacci tiene " + ultimo.toString().length() + " dígitos");
    }
}


//Recursivo

/*import java.math.BigInteger;
import java.util.HashMap;

public class PRACT3_SeriedeFibonnacci{
    
    // Cache para memoización
    private static HashMap<Integer, BigInteger> cache = new HashMap<>();
    
    // Función recursiva con memoización
    public static BigInteger fib(int n) {
        if (n < 2) {
            return BigInteger.valueOf(n);
        }
        if (cache.containsKey(n)) {
            return cache.get(n);
        }
        BigInteger result = fib(n - 1).add(fib(n - 2));
        cache.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        int n = 10000;

        long inicio = System.currentTimeMillis();

        // Generar serie
        BigInteger[] serie = new BigInteger[n];
        for (int i = 0; i < n; i++) {
            serie[i] = fib(i);
        }

        long fin = System.currentTimeMillis();

        System.out.println("Se generaron " + n + " números de Fibonacci");
        System.out.println("⏱ Tiempo: " + (fin - inicio) + " ms");

        // Mostrar primeros 20
        System.out.println("\nPrimeros 20 números de Fibonacci:");
        for (int i = 0; i < 20; i++) {
            System.out.println("F(" + i + ") = " + serie[i]);
        }

        // Mostrar tamaño del último número
        BigInteger ultimo = serie[n - 1];
        System.out.println("\nNúmero " + n + " de Fibonacci tiene " + ultimo.toString().length() + " dígitos");
    }
}"""
        
        """;
*/