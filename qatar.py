import tkinter as tk
import requests
import my_json
import json
from PIL import Image, ImageTk
from io import BytesIO

class Partidos:
    def obtener_resultados(self):
        self.api = "https://worldcupjson.net/matches/"  # Reemplaza con la URL correcta de la API
        response = requests.get(self.api)
        data = json.loads(response.text)
        print(data)  # Muestra la respuesta de la API en la consola

ventana = tk.Tk()
ventana.title("Qatar")

etiqueta_ciudad = tk.Label(ventana, text="Ingrese Partido:")
etiqueta_ciudad.pack()
entrada_ciudad = tk.Entry(ventana)
entrada_ciudad.pack()
    
boton_obtener_clima = tk.Button(ventana, text="Ingresar",command= my_json.obtener_partidos_random)
boton_obtener_clima.pack()

etiqueta_resultado = tk.Label(ventana)
etiqueta_resultado.pack()

ventana.mainloop()