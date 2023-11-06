import tkinter as tk
from tkinter import ttk
import requests

def obtener_datos_api():
    api_url = "https://worldcupjson.net/matches/"
    response = requests.get(api_url)
    data = response.json()  # Parsear la respuesta JSON

    # Filtrar y organizar los datos que deseas mostrar en el Treeview
    partidos = []
    for partido in data:
        equipo_local = partido["home_team_country"]
        goles_local = partido["home_team"]["goals"]
        equipo_visitante = partido["away_team_country"]
        goles_visitante = partido["away_team"]["goals"]
        partidos.append({"equipo_local": equipo_local, "goles_local": goles_local, "equipo_visitante": equipo_visitante, "goles_visitante": goles_visitante})

    return partidos

def mostrar_en_treeview():
    datos = obtener_datos_api()

    # Borrar elementos anteriores del Treeview
    for item in tabla.get_children():
        tabla.delete(item)

    # Agregar los nuevos datos al Treeview
    for dato in datos:
        tabla.insert("", "end", values=(dato["equipo_local"], dato["goles_local"], dato["equipo_visitante"], dato["goles_visitante"]))

ventana = tk.Tk()
ventana.title("Partidos de la Copa del Mundo")

tabla = ttk.Treeview(columns=("Equipo Local", "Goles Local", "Equipo Visitante", "Goles Visitante"))

tabla.heading("Equipo Local", text="Equipo Local")
tabla.heading("Goles Local", text="Goles Local")
tabla.heading("Equipo Visitante", text="Equipo Visitante")
tabla.heading("Goles Visitante", text="Goles Visitante")

tabla.grid()

boton_obtener_datos = tk.Button(ventana, text="Obtener Datos", command=mostrar_en_treeview)
boton_obtener_datos.grid()

ventana.mainloop()