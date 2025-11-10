from bisect import bisect_left

# CLASE NODO (para lista enlazada de ingredientes)
class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

# CLASE LISTA DE INGREDIENTES
class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    # a) Imprimir la lista de ingredientes
    def mostrar(self):
        if not self.cabeza:
            print("  (sin ingredientes)")
            return
        actual = self.cabeza
        while actual:
            print(f"  - {actual.nombre}")
            actual = actual.siguiente

    # Insertar ingrediente en orden alfabético
    def insertar(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            return
        nuevo = NodoIngrediente(nombre)

        # Caso: lista vacía o va al inicio
        if not self.cabeza or nombre.lower() < self.cabeza.nombre.lower():
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        # Recorrer hasta encontrar posición
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.nombre.lower() < nombre.lower():
            actual = actual.siguiente
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    # c) Eliminar un ingrediente
    def eliminar(self, nombre):
        if not self.cabeza:
            print("  No hay ingredientes en la lista.")
            return
        if self.cabeza.nombre.lower() == nombre.lower():
            self.cabeza = self.cabeza.siguiente
            print(f"  Ingrediente '{nombre}' eliminado.")
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.nombre.lower() != nombre.lower():
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            print(f"  Ingrediente '{nombre}' eliminado.")
        else:
            print("  Ingrediente no encontrado.")

    # Eliminar duplicados
    def depurar(self):
        vistos = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.nombre.lower() in vistos:
                previo.siguiente = actual.siguiente
            else:
                vistos.add(actual.nombre.lower())
                previo = actual
            actual = actual.siguiente

# CLASE POSTRE
class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaIngredientes()

# CLASE LIBRO DE POSTRES (ARREGLO ORDENADO)
class LibroDePostres:
    def __init__(self):
        self.postres = []

    # Buscar posición por orden alfabético
    def _indice(self, nombre):
        nombres = [p.nombre.lower() for p in self.postres]
        return bisect_left(nombres, nombre.lower())

    # Buscar un postre
    def buscar(self, nombre):
        i = self._indice(nombre)
        if i < len(self.postres) and self.postres[i].nombre.lower() == nombre.lower():
            return self.postres[i]
        return None

    # Alta de postre con ingredientes
    def alta_postre(self, nombre, ingredientes):
        nombre = nombre.strip()
        if self.buscar(nombre):
            print("Ese postre ya existe.")
            return
        nuevo = Postre(nombre)
        for ing in ingredientes:
            nuevo.ingredientes.insertar(ing)
        i = self._indice(nombre)
        self.postres.insert(i, nuevo)
        print(f"Postre '{nombre}' dado de alta.")

    # Baja de postre completo
    def baja_postre(self, nombre):
        i = self._indice(nombre)
        if i < len(self.postres) and self.postres[i].nombre.lower() == nombre.lower():
            self.postres.pop(i)
            print(f"Postre '{nombre}' eliminado.")
        else:
            print("Postre no encontrado.")

    # Mostrar ingredientes de un postre
    def mostrar_ingredientes(self, nombre):
        p = self.buscar(nombre)
        if not p:
            print("Postre no encontrado.")
            return
        print(f"\nIngredientes de {p.nombre}:")
        p.ingredientes.mostrar()

    # Insertar nuevos ingredientes
    def agregar_ingredientes(self, nombre, nuevos):
        p = self.buscar(nombre)
        if not p:
            print("Postre no encontrado.")
            return
        for ing in nuevos:
            p.ingredientes.insertar(ing)
        print("Ingredientes agregados correctamente.")

    # Eliminar un ingrediente
    def eliminar_ingrediente(self, nombre_postre, nombre_ingrediente):
        p = self.buscar(nombre_postre)
        if not p:
            print("Postre no encontrado.")
            return
        p.ingredientes.eliminar(nombre_ingrediente)

    # Mostrar todos los postres
    def mostrar_postres(self):
        print("\nPostres registrados:")
        for p in self.postres:
            print(f"- {p.nombre}")

    # 2) Eliminar elementos repetidos (postres e ingredientes)
    def depurar_todo(self):
        # Eliminar postres duplicados
        unicos = {}
        for p in self.postres:
            if p.nombre.lower() not in unicos:
                unicos[p.nombre.lower()] = p
            else:
                # Fusionar ingredientes si el postre ya existía
                actual = p.ingredientes.cabeza
                while actual:
                    unicos[p.nombre.lower()].ingredientes.insertar(actual.nombre)
                    actual = actual.siguiente
        self.postres = list(unicos.values())

        # Eliminar ingredientes repetidos en cada postre
        for p in self.postres:
            p.ingredientes.depurar()

        print("\nDepuración completada. Postres y duplicados eliminados.")

# MENÚ PRINCIPAL
def menu():
    libro = LibroDePostres()

    while True:
        print("""
=========== MENÚ PANADERÍA ===========
1. Alta de postre
2. Baja de postre
3. Mostrar todos los postres
4. Ver ingredientes de un postre
5. Agregar ingredientes a un postre
6. Eliminar un ingrediente
7. Depurar duplicados
8. Salir
======================================
        """)
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre del postre: ")
            ingredientes = input("Ingredientes (separados por coma): ").split(",")
            libro.alta_postre(nombre, [i.strip() for i in ingredientes if i.strip()])

        elif op == "2":
            nombre = input("Nombre del postre a eliminar: ")
            libro.baja_postre(nombre)

        elif op == "3":
            libro.mostrar_postres()

        elif op == "4":
            nombre = input("Nombre del postre: ")
            libro.mostrar_ingredientes(nombre)

        elif op == "5":
            nombre = input("Nombre del postre: ")
            nuevos = input("Nuevos ingredientes (separados por coma): ").split(",")
            libro.agregar_ingredientes(nombre, [i.strip() for i in nuevos if i.strip()])

        elif op == "6":
            postre = input("Nombre del postre: ")
            ing = input("Ingrediente a eliminar: ")
            libro.eliminar_ingrediente(postre, ing)

        elif op == "7":
            libro.depurar_todo()

        elif op == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

# EJECUCIÓN
if __name__ == "__main__":
    menu()
