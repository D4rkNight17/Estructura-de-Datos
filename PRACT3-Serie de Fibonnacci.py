#Iterativo

"Python"
import time
from sympy import fibonacci

n = 10000

inicio = time.time()
serie = [fibonacci(i) for i in range(n)]
fin = time.time()

print(f"Se generaron {n} números de Fibonacci")
print("⏱️ Tiempo:", round(fin - inicio, 6), "segundos")
print(serie[:10000])
print(f"\nNúmero {n} de Fibonacci tiene {len(str(serie[-1]))} dígitos")


#Recursivo

import time
from functools import lru_cache

# Función recursiva con cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Cantidad de números
n = 10000

inicio = time.time()
serie = [fib(i) for i in range(n)]
fin = time.time()

print(f"Se generaron {n} números de Fibonacci")
print("⏱️ Tiempo:", round(fin - inicio, 6), "segundos")

# Mostrar algunos resultados
print("\nPrimeros 20 números de Fibonacci:")
print(serie[:20])

print(f"\nNúmero {n} de Fibonacci tiene {len(str(serie[-1]))} dígitos")
