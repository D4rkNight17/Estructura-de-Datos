class Nodo:
    """Representa un nodo en la lista enlazada."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class MyLinkedList:
    """Implementa una lista enlazada simple con operaciones básicas."""
    def __init__(self):
        self.cabeza = None

    # Verifica si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Inserta un elemento al inicio
    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Inserta un elemento al final
    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar un elemento por valor
    def eliminar(self, dato):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(f"Elemento {dato} eliminado.")
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            print(f"Elemento {dato} eliminado.")
        else:
            print("Elemento no encontrado.")

    # Buscar un elemento
    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    # Mostrar todos los elementos
    def mostrar(self):
        if self.esta_vacia():
            print("La lista está vacía.")
        else:
            actual = self.cabeza
            while actual:
                print(f"[ {actual.dato} ] -> ", end="")
                actual = actual.siguiente
            print("None")

    # Contar nodos
    def contar_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador