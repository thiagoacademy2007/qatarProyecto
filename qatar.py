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
ventana.title("Partidos/Leagues Cup")
ventana.geometry("240x450")


# Frame1
frame1 = tk.Frame(ventana)
frame1.grid(row=1, column=1)

subtitulo = tk.Label(frame1, text="Final", font=("Ubuntu", 14))
subtitulo.grid(row=0, column=3, sticky="w",padx=5, pady=5)  # Alineado a la izquierda

#Frame 2
frame2 = tk.Frame(ventana)
frame2.grid(row=1, column=1)

entry = tk.Entry(frame1, width=1)
entry.grid(row=1, column=3, padx=4, pady=4)  # Agregamos espacio alrededor del Entry

entry2 = tk.Entry(frame1, width=1)
entry2.grid(row=1, column=4, padx=5, pady=5) 

imagen_url = "https://logodownload.org/wp-content/uploads/2016/11/argentina-national-football-team-logo-5.png"
response = requests.get(imagen_url)
imagen_data = BytesIO(response.content)
image = Image.open(imagen_data)
nuevo_ancho = 75
nuevo_alto = 75
image = image.resize((nuevo_ancho, nuevo_alto), Image.BOX)
photo = ImageTk.PhotoImage(image)
imagen1 = tk.Label(frame1, image=photo)
imagen1.grid(row=1, column=0)

#imagen 2 
imagen2_url ="https://logodownload.org/wp-content/uploads/2022/07/saudi-arabia-national-football-team-logo.png"
response = requests.get(imagen2_url)
imagen2_data = BytesIO(response.content)
image2 = Image.open(imagen2_data)
nuevo_ancho = 75  # Puedes cambiar estos valores si es necesario
nuevo_alto = 75
image2 = image2.resize((nuevo_ancho, nuevo_alto), Image.BOX)
photo2 = ImageTk.PhotoImage(image2)
img2 = tk.Label(frame1, image=photo2)
img2.grid(row=1, column=5)

#Frame 3
frame3 = tk.Frame(ventana)
frame3.grid(row=1, column=1)

button = tk.Button(frame1, text="Aceptar", command=my_json.obtener_partidos_random)
button.grid(row=2, column=3, columnspan=2)  # Centrado y ocupa 2 columnas

def cerrar():
    ventana.destroy()
    print("Gracias por su participación")

button1 = tk.Button(frame1, text="cerrar", command=cerrar)
button1.grid(row=3, column=3, columnspan=2)  # Centrado y ocupa 2 columnas

partido = input("Partido:")
c = Partidos()
c.obtener_resultados()

ventana.mainloop()