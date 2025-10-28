pila = []
TOPE = 0
MAX = 8

def mostrar_estado():
    print("\nEstado actual de la pila:")
    for i in range(len(pila)-1, -1, -1):
        if i == TOPE - 1:
            print(f"[{pila[i]}]  <-- TOPE")
        else:
            print(f"[{pila[i]}]")
    if not pila:
        print("[VACÍA]")
    print(f"TOPE = {TOPE}")
    print("-" * 30)

def insertar(elemento):
    global TOPE
    if TOPE < MAX:
        pila.append(elemento)
        TOPE += 1
        print(f"Insertar({elemento})")
    else:
        print("❌ Pila llena. No se puede insertar.")
    mostrar_estado()

def eliminar(variable):
    global TOPE
    if TOPE > 0:
        valor = pila.pop()
        TOPE -= 1
        print(f"Eliminar({variable}) → {variable} = {valor}")
    else:
        print(f"❌ Pila vacía. No se puede eliminar {variable}.")
    mostrar_estado()

# Secuencia de operaciones
insertar("X")   # a
insertar("Y")   # b
eliminar("Z")   # c
eliminar("T")   # d
eliminar("U")   # e
insertar("V")   # f
insertar("W")   # g
eliminar("p")   # h
insertar("R")   # i
