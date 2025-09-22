# Programa de ventas mensuales (Python)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
departamentos = ["Ropa", "Deportes", "Juguetería"]

# Crear matriz 12x3 inicializada en 0
ventas = [[0 for _ in departamentos] for _ in meses]

# 1. Insertar venta
def insertar_venta(mes, depto, valor):
    i = meses.index(mes)
    j = departamentos.index(depto)
    ventas[i][j] = valor

# 2. Buscar venta
def buscar_venta(mes, depto):
    i = meses.index(mes)
    j = departamentos.index(depto)
    return ventas[i][j]

# 3. Eliminar venta (poner 0)
def eliminar_venta(mes, depto):
    i = meses.index(mes)
    j = departamentos.index(depto)
    ventas[i][j] = 0

# 4. Imprimir tabla
def imprimir_tabla():
    print(f"{'':<10}", end="")
    for depto in departamentos:
        print(f"{depto:<12}", end="")
    print()
    for i, mes in enumerate(meses):
        print(f"{mes:<10}", end="")
        for j in range(len(departamentos)):
            print(f"{ventas[i][j]:<12}", end="")
        print()

# Ejemplo de uso
insertar_venta("Enero", "Ropa", 1500)
insertar_venta("Febrero", "Deportes", 2000)
insertar_venta("Diciembre", "Juguetería", 3000)

imprimir_tabla()

print("\nBuscar Febrero - Deportes:", buscar_venta("Febrero", "Deportes"))

eliminar_venta("Febrero", "Deportes")
print("Venta eliminada.")
imprimir_tabla()
