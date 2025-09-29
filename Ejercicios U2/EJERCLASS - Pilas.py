# Pila de ventas (vacía al inicio)
pila_ventas = []

while True:
    print("\n--- Menú de Ventas ---")
    print("1. Registrar una venta (apilar)")
    print("2. Deshacer última venta (desapilar)")
    print("3. Ver última venta")
    print("4. Mostrar todas las ventas")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        producto = input("Ingrese el producto vendido: ")
        pila_ventas.append(producto)  # Apilar
        print(f"Venta registrada: {producto}")

    elif opcion == "2":
        if pila_ventas:
            ultima = pila_ventas.pop()  # Desapilar
            print(f"Se deshizo la venta de: {ultima}")
        else:
            print("No hay ventas para deshacer.")

    elif opcion == "3":
        if pila_ventas:
            print(f"Última venta: {pila_ventas[-1]}")
        else:
            print("No hay ventas registradas.")

    elif opcion == "4":
        if pila_ventas:
            print("Ventas realizadas (de la primera a la última):")
            for venta in pila_ventas:
                print("-", venta)
        else:
            print("No hay ventas registradas.")

    elif opcion == "5":
        print("Saliendo del sistema de ventas...")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
