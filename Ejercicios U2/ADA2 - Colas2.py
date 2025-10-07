class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# Diccionario para almacenar las colas de cada servicio
colas_servicio = {}

# Contadores de turnos por servicio
contador_turnos = {}

print("=== Sistema de Atención de Compañía de Seguros ===")
print("Comandos:")
print("C<servicio> → Cliente llega. Ej: C1, C2, C3")
print("A<servicio> → Atender cliente. Ej: A1, A2, A3")
print("S → Salir del sistema\n")

while True:
    entrada = input("Ingrese una opción: ").strip().upper()

    if entrada == "S":
        print("Saliendo del sistema...")
        break

    # Llegada de cliente: C#
    if entrada.startswith("C"):
        servicio = entrada[1:]

        # Si no existe la cola, se crea
        if servicio not in colas_servicio:
            colas_servicio[servicio] = Cola()
            contador_turnos[servicio] = 0

        # Generar número de atención
        contador_turnos[servicio] += 1
        numero = contador_turnos[servicio]

        # Encolar cliente
        colas_servicio[servicio].encolar(numero)
        print(f"Cliente agregado al servicio {servicio} con número {numero}.")

    # Atender cliente: A#
    elif entrada.startswith("A"):
        servicio = entrada[1:]
        if servicio not in colas_servicio or colas_servicio[servicio].esta_vacia():
            print(f"No hay clientes en espera para el servicio {servicio}.")
        else:
            numero = colas_servicio[servicio].desencolar()
            print(f"Atendiendo cliente número {numero} del servicio {servicio}.")

    else:
        print("Comando no válido. Intente de nuevo.")