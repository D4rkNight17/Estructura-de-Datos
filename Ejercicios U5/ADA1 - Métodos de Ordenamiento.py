import time  # ⬅ para medir tiempos

def detectar_lista(texto):
    partes = texto.split()
    # Se considera lista SOLO si hay 2 o más números
    return len(partes) > 1 and all(p.isdigit() for p in partes)


def burbuja_pasos(lista):
    pasos = []
    contador = 0
    pasos.append(f"Inicio: {lista}")

    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            contador += 1
            pasos.append(f"Comparando {lista[j]} y {lista[j+1]}")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                pasos.append(f"Intercambio → {lista}")
    pasos.append(f"Resultado final: {lista}")
    return pasos, contador


def insercion_pasos(lista):
    pasos = []
    contador = 0
    pasos.append(f"Inicio: {lista}")

    for i in range(1, len(lista)):
        key = lista[i]
        pasos.append(f"Tomando clave = {key}")

        j = i - 1
        while j >= 0 and lista[j] > key:
            contador += 1
            pasos.append(f"{key} < {lista[j]} → mover {lista[j]} a derecha")
            lista[j + 1] = lista[j]
            pasos.append(f"Lista: {lista}")
            j -= 1

        lista[j + 1] = key
        pasos.append(f"Insertando clave → {lista}")

    pasos.append(f"Resultado final: {lista}")
    return pasos, contador


def seleccion_pasos(lista):
    pasos = []
    contador = 0
    pasos.append(f"Inicio: {lista}")
    n = len(lista)

    for i in range(n):
        min_idx = i
        pasos.append(f"Posición {i}: buscar mínimo desde índice {i}")

        for j in range(i + 1, n):
            contador += 1
            pasos.append(f"Comparando {lista[min_idx]} y {lista[j]}")
            if lista[j] < lista[min_idx]:
                pasos.append(f"Nuevo mínimo encontrado → {lista[j]}")
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        pasos.append(f"Intercambio final en posición {i} → {lista}")

    pasos.append(f"Resultado final: {lista}")
    return pasos, contador


# ================= MENÚ PRINCIPAL =================

def menu():
    lista_temporal = None

    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Ordenamiento Burbuja")
        print("2. Ordenamiento por Inserción")
        print("3. Ordenamiento por Selección")
        print("4. Salir")
        print("=================================")

        opcion = input("Selecciona una opción (o pega tu lista): ")

        # Detección inteligente de lista
        if detectar_lista(opcion):
            lista_temporal = list(map(int, opcion.split()))
            print("\nLista detectada correctamente ✔")
            print("Ahora elige un método de ordenamiento.\n")
            continue

        if opcion == "4":
            print("Programa finalizado. 👋")
            break

        if opcion not in ["1", "2", "3"]:
            print("❌ Opción no válida.")
            continue

        # Cargar lista si ya fue detectada antes
        if lista_temporal is not None:
            lista = lista_temporal
            lista_temporal = None
        else:
            numeros = input("\nIngresa los números separados por espacios: ")
            lista = list(map(int, numeros.split()))

        print("\n===== MOSTRANDO PASO A PASO =====\n")

        # MEDIR TIEMPO
        inicio_tiempo = time.time()

        if opcion == "1":
            pasos, contador = burbuja_pasos(lista)
            metodo = "BURBUJA"
        elif opcion == "2":
            pasos, contador = insercion_pasos(lista)
            metodo = "INSERCIÓN"
        else:
            pasos, contador = seleccion_pasos(lista)
            metodo = "SELECCIÓN"

        fin_tiempo = time.time()
        tiempo_ms = (fin_tiempo - inicio_tiempo) * 1000

        print(f"--- Ordenamiento por {metodo} ---")

        for p in pasos:
            print(p)

        print(f"\n➡ TOTAL DE PASOS REALIZADOS: {contador}")
        print(f"⏱ TIEMPO DE EJECUCIÓN: {tiempo_ms:.3f} ms")

        input("\nPresiona ENTER para volver al menú...")

menu()


