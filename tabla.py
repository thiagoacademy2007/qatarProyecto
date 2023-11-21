import tkinter as tk
from tkinter import ttk
import requests
import json

class Partidos:
    def obtener_resultados(self):
        # URL de la API que proporciona los resultados
        api_url = "https://worldcupjson.net/matches/"

        try:
            # Realizar una solicitud GET a la API
            response = requests.get(api_url)

            # Verificar si la solicitud fue exitosa (código de respuesta 200)
            if response.status_code == 200:
                # Parsear la respuesta JSON
                resultados = json.loads(response.text)
                return resultados
            else:
                print("Error al obtener los resultados. Código de respuesta:", response.status_code)
                return None
        except Exception as e:
            print("Error al obtener los resultados:", str(e))
            return None

# Crear una ventana de Tkinter
ventana = tk.Tk()
ventana.title("Qatar")
ventana.geometry("1000x600")

# Crear un Treeview para mostrar la tabla de partidos y resultados
tree = ttk.Treeview(ventana, columns=("ID", "Equipo Local", "Goles Local", "Equipo Visitante", "Goles Visitante"), height=30)
tree.heading("#1", text="ID")
tree.heading("#2", text="Equipo Local")
tree.heading("#3", text="Goles Local")
tree.heading("#4", text="Equipo Visitante")
tree.heading("#5", text="Goles Visitante")
tree.pack()

# Función para cargar los resultados en el Treeview
def cargar_resultados():
    c = Partidos()
    resultados = c.obtener_resultados()

    if resultados is not None:
        for resultado in resultados:
            # Agregar una fila a la tabla con los datos del resultado
            tree.insert("", "end", values=(resultado["id"],
                                          resultado["home_team"]["country"],
                                          resultado["home_team"]["goals"],
                                          resultado["away_team"]["country"],
                                          resultado["away_team"]["goals"]))

# Botón para cargar los resultados
button_cargar = tk.Button(ventana, text="Cargar Resultados", command=cargar_resultados)
button_cargar.pack()

ventana.mainloop()
