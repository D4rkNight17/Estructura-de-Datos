import tkinter as tk
from tkinter import messagebox

# ===============================
#   CLASES LÓGICAS DE LA LISTA
# ===============================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Inserta un nuevo nodo al final de la lista"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, data):
        """Busca un valor en la lista y devuelve True si lo encuentra"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        """Elimina un nodo con el valor indicado"""
        if not self.head:
            return False

        # Caso 1: el primer nodo es el que se quiere eliminar
        if self.head.data == data:
            self.head = self.head.next
            return True

        # Caso 2: buscar en el resto de la lista
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def traverse(self):
        """Recorre la lista y devuelve una lista de valores"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


# ===============================
#   INTERFAZ GRÁFICA (Tkinter)
# ===============================

class LinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista Enlazada Visual 🧠")
        self.root.geometry("800x500")
        self.root.configure(bg="#F4F6F7")

        self.linked_list = LinkedList()

        # Entrada de texto
        self.entry = tk.Entry(root, font=("Segoe UI", 12))
        self.entry.pack(pady=10)

        # Botones de acciones
        frame_buttons = tk.Frame(root, bg="#F4F6F7")
        frame_buttons.pack()

        tk.Button(frame_buttons, text="➕ Insertar", command=self.insert_node, width=15, bg="#58D68D").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_buttons, text="🔍 Buscar", command=self.search_node, width=15, bg="#5DADE2").grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_buttons, text="❌ Eliminar", command=self.delete_node, width=15, bg="#EC7063").grid(row=0, column=2, padx=5, pady=5)
        tk.Button(frame_buttons, text="🔁 Recorrer", command=self.traverse_list, width=15, bg="#F4D03F").grid(row=0, column=3, padx=5, pady=5)

        # Canvas para mostrar los nodos
        self.canvas = tk.Canvas(root, width=760, height=350, bg="white", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Etiqueta para mostrar resultados
        self.label_info = tk.Label(root, text="", font=("Segoe UI", 11, "bold"), bg="#F4F6F7", fg="#2E4053")
        self.label_info.pack(pady=5)

    def insert_node(self):
        value = self.entry.get().strip()
        if not value:
            messagebox.showwarning("Error", "Debes ingresar un valor.")
            return
        self.linked_list.insert(value)
        self.entry.delete(0, tk.END)
        self.draw_list()
        self.label_info.config(text=f"Nodo '{value}' insertado correctamente ✅")

    def search_node(self):
        value = self.entry.get().strip()
        if not value:
            messagebox.showwarning("Error", "Ingresa un valor a buscar.")
            return
        found = self.linked_list.search(value)
        self.draw_list(highlight=value if found else None)
        if found:
            self.label_info.config(text=f"Nodo '{value}' encontrado 🔎")
        else:
            self.label_info.config(text=f"Nodo '{value}' no encontrado ❌")

    def delete_node(self):
        value = self.entry.get().strip()
        if not value:
            messagebox.showwarning("Error", "Ingresa un valor a eliminar.")
            return
        deleted = self.linked_list.delete(value)
        self.entry.delete(0, tk.END)
        self.draw_list()
        if deleted:
            self.label_info.config(text=f"Nodo '{value}' eliminado correctamente 🗑️")
        else:
            self.label_info.config(text=f"No se encontró el nodo '{value}' ⚠️")

    def traverse_list(self):
        nodes = self.linked_list.traverse()
        if not nodes:
            self.label_info.config(text="La lista está vacía 💤")
        else:
            self.label_info.config(text=f"Recorrido: {' → '.join(nodes)}")
        self.draw_list()

    def draw_list(self, highlight=None):
        """Dibuja los nodos en el canvas"""
        self.canvas.delete("all")

        nodes = self.linked_list.traverse()
        if not nodes:
            self.canvas.create_text(380, 175, text="(lista vacía)", font=("Segoe UI", 12, "italic"), fill="#7B7D7D")
            return

        x, y = 60, 150
        for i, data in enumerate(nodes):
            color = "#5DADE2" if data == highlight else "#58D68D"
            # Dibuja el nodo
            self.canvas.create_rectangle(x, y, x + 80, y + 40, fill=color, outline="black")
            self.canvas.create_text(x + 40, y + 20, text=str(data), font=("Segoe UI", 12, "bold"), fill="white")

            # Dibuja la flecha (→) entre nodos
            if i < len(nodes) - 1:
                self.canvas.create_line(x + 80, y + 20, x + 120, y + 20, arrow=tk.LAST, width=2)
                x += 120

        # Si se sale del canvas, muestra aviso
        if len(nodes) > 6:
            self.canvas.create_text(700, 300, text="(La lista continúa...)", font=("Segoe UI", 10, "italic"), fill="#7B7D7D")


# ===============================
#     PROGRAMA PRINCIPAL
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()
