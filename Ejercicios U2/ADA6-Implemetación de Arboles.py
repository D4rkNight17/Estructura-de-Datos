from collections import deque
import tkinter as tk

# ===================================================
#                 CLASE NODO
# ===================================================
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


# ===================================================
#        CLASE ÁRBOL BINARIO DE BÚSQUEDA
# ===================================================
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # [0] ¿El árbol está vacío?
    def es_vacio(self):
        return self.raiz is None

    # [1] Insertar elemento
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar_rec(self.raiz, dato)

    def _insertar_rec(self, nodo, dato):
        if dato == nodo.dato:
            print("El valor ya existe.")
        elif dato < nodo.dato:
            if nodo.izq:
                self._insertar_rec(nodo.izq, dato)
            else:
                nodo.izq = Nodo(dato)
        else:
            if nodo.der:
                self._insertar_rec(nodo.der, dato)
            else:
                nodo.der = Nodo(dato)

    # [2] Mostrar árbol acostado
    def mostrar_acostado(self):
        if self.es_vacio():
            print("Árbol vacío.")
        else:
            self._mostrar_rec(self.raiz, 0)

    def _mostrar_rec(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_rec(nodo.der, nivel + 1)
            print("    " * nivel + f"{nodo.dato}")
            self._mostrar_rec(nodo.izq, nivel + 1)

    # [3] Graficar árbol completo (Tkinter)
    def graficar(self):
        if self.es_vacio():
            print("Árbol vacío.")
            return
        ArbolGrafico(self).mostrar("Árbol Binario de Búsqueda")

    # [4] Buscar elemento
    def buscar(self, dato):
        return self._buscar_rec(self.raiz, dato)

    def _buscar_rec(self, nodo, dato):
        if nodo is None:
            return False
        if dato == nodo.dato:
            return True
        elif dato < nodo.dato:
            return self._buscar_rec(nodo.izq, dato)
        else:
            return self._buscar_rec(nodo.der, dato)

    # [5] Recorrido PreOrden
    def preorden(self):
        resultado = []
        self._preorden_rec(self.raiz, resultado)
        return resultado

    def _preorden_rec(self, nodo, res):
        if nodo:
            res.append(nodo.dato)
            self._preorden_rec(nodo.izq, res)
            self._preorden_rec(nodo.der, res)

    # [6] Recorrido InOrden
    def inorden(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, res):
        if nodo:
            self._inorden_rec(nodo.izq, res)
            res.append(nodo.dato)
            self._inorden_rec(nodo.der, res)

    # [7] Recorrido PostOrden
    def postorden(self):
        resultado = []
        self._postorden_rec(self.raiz, resultado)
        return resultado

    def _postorden_rec(self, nodo, res):
        if nodo:
            self._postorden_rec(nodo.izq, res)
            self._postorden_rec(nodo.der, res)
            res.append(nodo.dato)

    # [8] Eliminar nodo con PREDECESOR
    def eliminar_predecesor(self, dato):
        self.raiz = self._eliminar(self.raiz, dato, predecesor=True)

    # [9] Eliminar nodo con SUCESOR
    def eliminar_sucesor(self, dato):
        self.raiz = self._eliminar(self.raiz, dato, predecesor=False)

    def _eliminar(self, nodo, dato, predecesor=True):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.izq = self._eliminar(nodo.izq, dato, predecesor)
        elif dato > nodo.dato:
            nodo.der = self._eliminar(nodo.der, dato, predecesor)
        else:
            # Caso sin hijos
            if nodo.izq is None and nodo.der is None:
                return None
            # Caso un hijo
            elif nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            # Caso dos hijos
            else:
                if predecesor:
                    reemplazo = self._maximo(nodo.izq)
                    nodo.dato = reemplazo.dato
                    nodo.izq = self._eliminar(nodo.izq, reemplazo.dato, predecesor)
                else:
                    reemplazo = self._minimo(nodo.der)
                    nodo.dato = reemplazo.dato
                    nodo.der = self._eliminar(nodo.der, reemplazo.dato, predecesor)
        return nodo

    def _maximo(self, nodo):
        while nodo.der:
            nodo = nodo.der
        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    # [10] Recorrer por niveles (Amplitud)
    def recorrer_niveles(self):
        if self.es_vacio():
            return []
        res = []
        cola = deque()
        cola.append(self.raiz)
        while cola:
            nodo = cola.popleft()
            res.append(nodo.dato)
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)
        return res

    # [11] Altura del árbol
    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

    # [12] Cantidad de hojas
    def contar_hojas(self):
        return self._contar_hojas(self.raiz)

    def _contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self._contar_hojas(nodo.izq) + self._contar_hojas(nodo.der)

    # [13] Cantidad de nodos
    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izq) + self._contar_nodos(nodo.der)

    # [15] Árbol binario completo
    def es_completo(self):
        if self.es_vacio():
            return True
        cola = deque()
        cola.append(self.raiz)
        encontrado_hueco = False
        while cola:
            nodo = cola.popleft()
            if nodo.izq:
                if encontrado_hueco:
                    return False
                cola.append(nodo.izq)
            else:
                encontrado_hueco = True
            if nodo.der:
                if encontrado_hueco:
                    return False
                cola.append(nodo.der)
            else:
                encontrado_hueco = True
        return True

    # [16] Árbol binario lleno
    def es_lleno(self):
        return self._es_lleno(self.raiz)

    def _es_lleno(self, nodo):
        if nodo is None:
            return True
        if nodo.izq is None and nodo.der is None:
            return True
        if nodo.izq and nodo.der:
            return self._es_lleno(nodo.izq) and self._es_lleno(nodo.der)
        return False

    # [17] Eliminar el árbol completo
    def eliminar_arbol(self):
        self.raiz = None


# ===================================================
#        CLASE PARA DIBUJAR EL ÁRBOL (Tkinter)
# ===================================================
class ArbolGrafico:
    def __init__(self, arbol):
        self.arbol = arbol

    def mostrar(self, titulo):
        ventana = tk.Tk()
        ventana.title(titulo)
        ventana.geometry("900x600")
        canvas = tk.Canvas(ventana, bg="white")
        canvas.pack(fill=tk.BOTH, expand=True)

        self._dibujar(canvas, self.arbol.raiz, 450, 50, 200)
        ventana.mainloop()

    def _dibujar(self, canvas, nodo, x, y, dx):
        if nodo is None:
            return
        radio = 20
        # Nodo
        canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="#AED6F1", outline="black")
        canvas.create_text(x, y, text=str(nodo.dato), font=("Segoe UI", 10, "bold"))
        # Enlaces
        if nodo.izq:
            canvas.create_line(x, y + radio, x - dx / 2, y + 80 - radio, arrow=tk.LAST)
            self._dibujar(canvas, nodo.izq, x - dx / 2, y + 80, dx / 2)
        if nodo.der:
            canvas.create_line(x, y + radio, x + dx / 2, y + 80 - radio, arrow=tk.LAST)
            self._dibujar(canvas, nodo.der, x + dx / 2, y + 80, dx / 2)


# ===================================================
#                   MENÚ PRINCIPAL
# ===================================================
def menu():
    arbol = ArbolBinarioBusqueda()

    while True:
        print("""
============== MENÚ ÁRBOL DE BÚSQUEDA ==============
[0] ¿Está vacío el árbol?
[1] Insertar elemento
[2] Mostrar árbol acostado (texto)
[3] Mostrar árbol gráfico (Tkinter)
[4] Buscar un elemento
[5] Recorrer PreOrden
[6] Recorrer InOrden
[7] Recorrer PostOrden
[8] Eliminar nodo (PREDECESOR)
[9] Eliminar nodo (SUCESOR)
[10] Recorrer por niveles (y mostrar gráfico)
[11] Altura del árbol
[12] Cantidad de hojas
[13] Cantidad de nodos
[15] ¿Es árbol binario completo?
[16] ¿Es árbol binario lleno?
[17] Eliminar el árbol completo
[18] Salir
=====================================================
        """)
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("¿Árbol vacío?:", "Sí" if arbol.es_vacio() else "No")
        elif opcion == "1":
            valor = int(input("Valor a insertar: "))
            arbol.insertar(valor)
            print("Insertado correctamente.")
        elif opcion == "2":
            arbol.mostrar_acostado()
        elif opcion == "3":
            arbol.graficar()
        elif opcion == "4":
            valor = int(input("Valor a buscar: "))
            print("Encontrado" if arbol.buscar(valor) else "No encontrado.")
        elif opcion == "5":
            print("PreOrden:", arbol.preorden())
        elif opcion == "6":
            print("InOrden:", arbol.inorden())
        elif opcion == "7":
            print("PostOrden:", arbol.postorden())
        elif opcion == "8":
            valor = int(input("Valor a eliminar (predecesor): "))
            arbol.eliminar_predecesor(valor)
            print("Nodo eliminado (PREDECESOR).")
        elif opcion == "9":
            valor = int(input("Valor a eliminar (sucesor): "))
            arbol.eliminar_sucesor(valor)
            print("Nodo eliminado (SUCESOR).")
        elif opcion == "10":
            print("Recorrido por niveles:", arbol.recorrer_niveles())
            arbol.graficar()
        elif opcion == "11":
            print("Altura del árbol:", arbol.altura())
        elif opcion == "12":
            print("Cantidad de hojas:", arbol.contar_hojas())
        elif opcion == "13":
            print("Cantidad de nodos:", arbol.contar_nodos())
        elif opcion == "15":
            print("¿Es completo?:", "Sí" if arbol.es_completo() else "No")
        elif opcion == "16":
            print("¿Es lleno?:", "Sí" if arbol.es_lleno() else "No")
        elif opcion == "17":
            arbol.eliminar_arbol()
            print("Árbol eliminado.")
        elif opcion == "18":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
