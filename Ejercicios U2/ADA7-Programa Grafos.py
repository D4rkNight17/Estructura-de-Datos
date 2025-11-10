import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# -------------------------------
# Ventana principal
# -------------------------------
ventana = tk.Tk()
ventana.title("Grafo Interactivo - Mapa de México")
ventana.geometry("1000x700")

# Crear figura con Basemap
fig, ax = plt.subplots(figsize=(7, 6))
m = Basemap(projection="merc", llcrnrlon=-118, llcrnrlat=14,
            urcrnrlon=-86, urcrnrlat=33, resolution="i", ax=ax)
m.drawmapboundary(fill_color="#A6CAE0")
m.fillcontinents(color="#FFE0B2", lake_color="#A6CAE0")
m.drawcountries(linewidth=1)
m.drawstates(linewidth=0.5)

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# -------------------------------
# Datos base
# -------------------------------
# Coordenadas aproximadas de los 32 estados
estados_coords = {
    "Baja California": (32.5, -115.5),
    "Baja California Sur": (24.0, -111.7),
    "Sonora": (29.1, -110.9),
    "Chihuahua": (28.6, -106.1),
    "Coahuila": (27.0, -102.0),
    "Nuevo León": (25.7, -100.3),
    "Tamaulipas": (24.3, -98.7),
    "Sinaloa": (25.8, -108.0),
    "Durango": (24.0, -104.7),
    "Zacatecas": (22.8, -102.6),
    "San Luis Potosí": (22.2, -100.9),
    "Nayarit": (21.8, -104.9),
    "Jalisco": (20.7, -103.3),
    "Colima": (19.2, -103.7),
    "Michoacán": (19.7, -101.2),
    "Guanajuato": (20.9, -101.3),
    "Querétaro": (20.6, -100.4),
    "Hidalgo": (20.1, -98.7),
    "Veracruz": (19.2, -96.1),
    "Puebla": (19.0, -98.2),
    "Tlaxcala": (19.3, -98.2),
    "CDMX": (19.4, -99.1),
    "Morelos": (18.9, -99.2),
    "Guerrero": (17.5, -99.5),
    "Oaxaca": (17.1, -96.7),
    "Chiapas": (16.7, -93.1),
    "Tabasco": (17.9, -92.6),
    "Campeche": (19.8, -90.5),
    "Yucatán": (20.9, -89.0),
    "Quintana Roo": (19.6, -88.0),
    "Aguascalientes": (21.9, -102.3)
}

# -------------------------------
# Crear grafo
# -------------------------------
grafo = nx.Graph()
posiciones = {}
seleccionados = []

# -------------------------------
# Funciones
# -------------------------------
def dibujar_mapa():
    """Dibuja todo el mapa de México con los nombres de los estados"""
    ax.clear()
    m.drawmapboundary(fill_color="#A6CAE0")
    m.fillcontinents(color="#FFE0B2", lake_color="#A6CAE0")
    m.drawcountries(linewidth=1)
    m.drawstates(linewidth=0.5)

    for estado, (lat, lon) in estados_coords.items():
        x, y = m(lon, lat)
        posiciones[estado] = (x, y)
        ax.plot(x, y, "o", color="green", markersize=6)
        ax.text(x, y, estado, fontsize=7, ha="center", va="bottom")

    canvas.draw()

def click_mapa(event):
    """Detecta clics sobre el mapa y selecciona hasta 7 estados"""
    if len(seleccionados) >= 7:
        messagebox.showwarning("Límite alcanzado", "Ya seleccionaste 7 estados.")
        return

    x_click, y_click = event.xdata, event.ydata
    if x_click is None or y_click is None:
        return

    estado_mas_cercano = None
    min_dist = float("inf")
    for estado, (x, y) in posiciones.items():
        dist = (x - x_click)**2 + (y - y_click)**2
        if dist < min_dist:
            min_dist = dist
            estado_mas_cercano = estado

    if estado_mas_cercano and estado_mas_cercano not in seleccionados:
        seleccionados.append(estado_mas_cercano)
        x, y = posiciones[estado_mas_cercano]
        ax.plot(x, y, "o", color="red", markersize=8)
        ax.text(x, y, estado_mas_cercano, fontsize=8, color="red", ha="center", va="bottom")
        canvas.draw()

        if len(seleccionados) == 7:
            conectar_estados()

def conectar_estados():
    """Crea conexiones aleatorias entre los estados seleccionados"""
    grafo.clear()
    for i in range(len(seleccionados) - 1):
        origen = seleccionados[i]
        destino = seleccionados[i + 1]
        costo = random.randint(200, 1500)
        grafo.add_edge(origen, destino, peso=costo)
    dibujar_grafo()

def dibujar_grafo():
    """Redibuja el grafo con los estados seleccionados y costos"""
    dibujar_mapa()
    nx.draw(grafo, posiciones, with_labels=False, node_color="red", node_size=400, ax=ax)
    etiquetas = nx.get_edge_attributes(grafo, 'peso')
    nx.draw_networkx_edge_labels(grafo, posiciones, edge_labels=etiquetas, font_size=8, ax=ax)
    canvas.draw()

def recorrido_sin_repetir():
    """Muestra el recorrido sin repetir y su costo total"""
    if len(seleccionados) < 7:
        messagebox.showwarning("Faltan estados", "Selecciona primero los 7 estados.")
        return
    recorrido = seleccionados
    costo_total = sum(grafo[recorrido[i]][recorrido[i + 1]]['peso'] for i in range(len(recorrido) - 1))
    messagebox.showinfo("Recorrido sin repetir", f"Ruta: {' → '.join(recorrido)}\nCosto total: {costo_total}")

def recorrido_repetido():
    """Muestra el recorrido con repetición y su costo total"""
    if len(seleccionados) < 7:
        messagebox.showwarning("Faltan estados", "Selecciona primero los 7 estados.")
        return
    recorrido = seleccionados + [seleccionados[random.randint(0, 6)], seleccionados[0]]
    costo_total = 0
    for i in range(len(recorrido) - 1):
        if grafo.has_edge(recorrido[i], recorrido[i + 1]):
            costo_total += grafo[recorrido[i]][recorrido[i + 1]]['peso']
        else:
            costo_total += random.randint(200, 1500)
    messagebox.showinfo("Recorrido con repetición", f"Ruta: {' → '.join(recorrido)}\nCosto total: {costo_total}")

def reiniciar():
    """Limpia todo y permite volver a seleccionar estados"""
    seleccionados.clear()
    grafo.clear()
    dibujar_mapa()
    messagebox.showinfo("Reiniciado", "Mapa y selecciones reiniciados. Puedes comenzar de nuevo.")

# -------------------------------
# Botones
# -------------------------------
frame_botones = tk.Frame(ventana)
frame_botones.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

tk.Button(frame_botones, text="Mostrar Mapa de México", command=dibujar_mapa,
          bg="#2196F3", fg="white").pack(pady=5, fill=tk.X)
tk.Button(frame_botones, text="Recorrido sin repetir", command=recorrido_sin_repetir,
          bg="#4CAF50", fg="white").pack(pady=5, fill=tk.X)
tk.Button(frame_botones, text="Recorrido con repetición", command=recorrido_repetido,
          bg="#FF9800", fg="white").pack(pady=5, fill=tk.X)
tk.Button(frame_botones, text="Reiniciar", command=reiniciar,
          bg="#9C27B0", fg="white").pack(pady=10, fill=tk.X)

# -------------------------------
# Eventos y arranque
# -------------------------------
canvas.mpl_connect("button_press_event", click_mapa)
dibujar_mapa()
ventana.mainloop()



