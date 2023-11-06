import tkinter as tk
from tkinter import ttk
import my_json

def agregar_partido():
    equipo_local = entrada_equipo_local.get()
    equipo_visitante = entrada_equipo_visitante.get()
    goles_local = entrada_goles_local.get()
    goles_visitante = entrada_goles_visitante.get()
    
    # Asegúrate de validar y procesar los datos según sea necesario
    # Por ejemplo, puedes convertir los goles en enteros si es necesario

    # Agregar los datos del partido al Treeview
    tabla.insert("", "end", values=(equipo_local, goles_local, equipo_visitante, goles_visitante))
    
ventana = tk.Tk()
ventana.title("Qatar 2022")

tabla = ttk.Treeview(columns=("Equipo Local", "Goles Local", "Equipo Visitante", "Goles Visitante"))

tabla.heading("Equipo Local", text="Equipo Local")
tabla.heading("Goles Local", text="Goles Local")
tabla.heading("Equipo Visitante", text="Equipo Visitante")
tabla.heading("Goles Visitante", text="Goles Visitante")

tabla.grid()

# Campos de entrada
etiqueta_equipo_local = tk.Label(ventana, text="Equipo Local:")
etiqueta_equipo_local.grid()
entrada_equipo_local = tk.Entry(ventana)
entrada_equipo_local.grid()

etiqueta_goles_local = tk.Label(ventana, text="Goles Local:")
etiqueta_goles_local.grid()
entrada_goles_local = tk.Entry(ventana)
entrada_goles_local.grid()

etiqueta_equipo_visitante = tk.Label(ventana, text="Equipo Visitante:")
etiqueta_equipo_visitante.grid()
entrada_equipo_visitante = tk.Entry(ventana)
entrada_equipo_visitante.grid()

etiqueta_goles_visitante = tk.Label(ventana, text="Goles Visitante:")
etiqueta_goles_visitante.grid()
entrada_goles_visitante = tk.Entry(ventana)
entrada_goles_visitante.grid()

# Botón para agregar partido
boton_agregar_partido = tk.Button(ventana, text="Agregar Partido", command=agregar_partido)
boton_agregar_partido.grid()

# Botón para obtener datos aleatorios
boton_obtener_datos = tk.Button(ventana, text="Obtener Partidos Aleatorios", command=my_json.obtener_partidos)
boton_obtener_datos.grid()

ventana.mainloop()
