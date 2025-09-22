# Programa de Ventas Mensuales (Python & Java)

Este proyecto contiene dos programas, uno en **Python** y otro en **Java**, que permiten administrar las **ventas mensuales** de tres departamentos de una tienda:

- Ropa 👕  
- Deportes 🏀  
- Juguetería 🧸  

Se utiliza un **arreglo bidimensional (matriz)** donde:  
- Las **filas** representan los meses del año (Enero a Diciembre).  
- Las **columnas** representan los departamentos.  
- Cada celda guarda el valor de la venta correspondiente.

---

## ⚙️ Funcionalidades

Ambos programas implementan los siguientes métodos:

### 1. Insertar venta
- **Python:** `insertar_venta(mes, depto, valor)`  
- **Java:** `insertarVenta(String mes, String depto, int valor)`  

Este método permite **registrar o actualizar** una venta en un mes y departamento específico.  
Ejemplo: `insertar_venta("Enero", "Ropa", 1500)` guarda 1500 en la celda de **Enero - Ropa**.

---

### 2. Buscar venta
- **Python:** `buscar_venta(mes, depto)`  
- **Java:** `buscarVenta(String mes, String depto)`  

Permite **consultar** la venta guardada en un mes y departamento.  
Ejemplo: `buscar_venta("Febrero", "Deportes")` devuelve el valor guardado en **Febrero - Deportes**.

---

### 3. Eliminar venta
- **Python:** `eliminar_venta(mes, depto)`  
- **Java:** `eliminarVenta(String mes, String depto)`  

Este método **borra** una venta específica colocando el valor en `0`.  
Ejemplo: `eliminar_venta("Febrero", "Deportes")` pone en `0` la celda de **Febrero - Deportes**.

---

### 4. Imprimir tabla
- **Python:** `imprimir_tabla()`  
- **Java:** `imprimirTabla()`  

Muestra en consola una **tabla formateada** con los meses como filas y los departamentos como columnas, junto con sus ventas registradas.


