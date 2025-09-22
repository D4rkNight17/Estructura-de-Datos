public class EJER_ARREGLOS01{
    static String[] meses = {"Enero","Febrero","Marzo","Abril","Mayo","Junio",
                             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};
    static String[] departamentos = {"Ropa","Deportes","Juguetería"};
    static int[][] ventas = new int[12][3];

    // 1. Insertar venta
    public static void insertarVenta(String mes, String depto, int valor) {
        int i = getIndiceMes(mes);
        int j = getIndiceDepto(depto);
        if (i != -1 && j != -1) {
            ventas[i][j] = valor;
        }
    }

    // 2. Buscar venta
    public static int buscarVenta(String mes, String depto) {
        int i = getIndiceMes(mes);
        int j = getIndiceDepto(depto);
        return (i != -1 && j != -1) ? ventas[i][j] : -1;
    }

    // 3. Eliminar venta (poner en 0)
    public static void eliminarVenta(String mes, String depto) {
        int i = getIndiceMes(mes);
        int j = getIndiceDepto(depto);
        if (i != -1 && j != -1) {
            ventas[i][j] = 0;
        }
    }

    // 4. Imprimir tabla
    public static void imprimirTabla() {
        System.out.printf("%-10s", "");
        for (String depto : departamentos) {
            System.out.printf("%-12s", depto);
        }
        System.out.println();
        for (int i = 0; i < meses.length; i++) {
            System.out.printf("%-10s", meses[i]);
            for (int j = 0; j < departamentos.length; j++) {
                System.out.printf("%-12d", ventas[i][j]);
            }
            System.out.println();
        }
    }

    // Auxiliares
    private static int getIndiceMes(String mes) {
        for (int i = 0; i < meses.length; i++) {
            if (meses[i].equalsIgnoreCase(mes)) return i;
        }
        return -1;
    }

    private static int getIndiceDepto(String depto) {
        for (int j = 0; j < departamentos.length; j++) {
            if (departamentos[j].equalsIgnoreCase(depto)) return j;
        }
        return -1;
    }

    // Ejemplo de uso
    public static void main(String[] args) {
        insertarVenta("Enero", "Ropa", 1500);
        insertarVenta("Febrero", "Deportes", 2000);
        insertarVenta("Diciembre", "Juguetería", 3000);

        imprimirTabla();

        System.out.println("\nBuscar Febrero - Deportes: " + buscarVenta("Febrero", "Deportes"));

        eliminarVenta("Febrero", "Deportes");
        System.out.println("Venta eliminada.");
        imprimirTabla();
    }
}
