from MyLinkedList import MyLinkedList

# Crear la lista
lista = MyLinkedList()

lista.insertar_al_final(10)
lista.insertar_al_final(20)
lista.insertar_al_inicio(5)

lista.mostrar()
print("Cantidad de nodos:", lista.contar_nodos())

print("Buscar 20:", lista.buscar(20))
print("Buscar 50:", lista.buscar(50))

lista.eliminar(10)
lista.mostrar()