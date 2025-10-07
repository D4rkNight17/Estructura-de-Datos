from queue import Queue

def sumar_colas(colaA, colaB):
    cola_resultado = Queue()
    while not colaA.empty() and not colaB.empty():
        a = colaA.get()
        b = colaB.get()
        cola_resultado.put(a + b)
    return cola_resultado


# Ejemplo de uso
colaA = Queue()
colaB = Queue()

# Agregamos los valores del ejemplo
for n in [3, 4, 2, 8, 12]:
    colaA.put(n)
for n in [6, 2, 9, 11, 3]:
    colaB.put(n)

# Obtenemos la cola resultado
cola_resultado = sumar_colas(colaA, colaB)

# Mostramos los resultados
print("Cola Resultado:")
while not cola_resultado.empty():
    print(cola_resultado.get())
