import tkinter as tk
from tkinter import messagebox

class PilaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pila - Ejemplo Gráfico")

        self.pila = []

        # Entrada
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Botones
        self.btn_apilar = tk.Button(root, text="Apilar", command=self.apilar, width=15, bg="lightgreen")
        self.btn_apilar.pack(pady=5)

        self.btn_desapilar = tk.Button(root, text="Desapilar", command=self.desapilar, width=15, bg="lightcoral")
        self.btn_desapilar.pack(pady=5)

        # Lienzo para mostrar la pila
        self.canvas = tk.Canvas(root, width=200, height=300, bg="white")
        self.canvas.pack(pady=10)

        self.dibujar_pila()

    def apilar(self):
        elemento = self.entry.get()
        if elemento:
            self.pila.append(elemento)
            self.entry.delete(0, tk.END)
            self.dibujar_pila()
        else:
            messagebox.showwarning("Advertencia", "Ingrese un elemento para apilar.")

    def desapilar(self):
        if self.pila:
            eliminado = self.pila.pop()
            messagebox.showinfo("Desapilar", f"Elemento eliminado: {eliminado}")
            self.dibujar_pila()
        else:
            messagebox.showwarning("Advertencia", "La pila está vacía.")

    def dibujar_pila(self):
        self.canvas.delete("all")
        x1, y1, x2, y2 = 50, 250, 150, 280
        for elemento in reversed(self.pila):
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")
            self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text=elemento, font=("Arial", 12))
            y1 -= 35
            y2 -= 35

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGUI(root)
    root.mainloop()
