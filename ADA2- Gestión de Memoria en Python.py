#Alumno: Manuel Armando Lara Puc        Grupo: 3SA

# Memoria Estática en Python
Calificaciones = [0] * 5  # lista de tamaño fijo 5
for i in range(5):
    Calificaciones[i] = int(input(f"Captura la calificación {i + 1}: "))
print("Calificaciones ingresadas:", Calificaciones)


"---------------------------------------------------------------------------------"


# Memoria Dinámica en Python
frutas = []  # lista vacía
# Agregar elementos
frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Uvas")
print("Lista inicial:", frutas)
# Eliminar elementos
frutas.pop(0)  # elimina el primer elemento (Mango)
frutas.pop(0)  # ahora elimina el nuevo primer elemento (Manzana)
# Agregar más elementos
frutas.append("Sandía")
print("Lista final:", frutas)
