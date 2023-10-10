import requests
import tkinter as tk

class Clima:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.api_key = "a724f8d8890824aa1326eb56e175ecf1"

    def obtener_clima(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.ciudad}&appid={self.api_key}&units=metric"
        respuesta = requests.get(url)
        clima_datos = respuesta.json()
        print(respuesta.json())
        if clima_datos["cod"] == 200:
            temperatura = clima_datos["main"]["temp"]
            humedad = clima_datos["main"]["humidity"]
            descripcion = clima_datos["weather"][0]["description"]
            resultado = f"Ciudad: {self.ciudad}\n"
            resultado += f"Temperatura: {temperatura}°C\n"
            resultado += f"Humedad: {humedad}%\n"
            resultado += f"Descripción del clima: {descripcion}"
        elif clima_datos["cod"] == "400":
            resultado = "No se ha escrito ninguna ciudad"      
        else:
            resultado = f"Ciudad: {self.ciudad}?\n"
            resultado += "No se ha encontro esta ciudad"

        etiqueta_resultado.config(text=resultado)

ventana = tk.Tk()
ventana.title("API Clima")

def obtener_clima():
    ciudad = entrada_ciudad.get()
    clima = Clima(ciudad)
    clima.obtener_clima()

etiqueta_ciudad = tk.Label(ventana, text="Ingrese una ciudad:")
etiqueta_ciudad.pack()
entrada_ciudad = tk.Entry(ventana)
entrada_ciudad.pack()
    
boton_obtener_clima = tk.Button(ventana, text="Obtener Clima", command=obtener_clima)
boton_obtener_clima.pack()

etiqueta_resultado = tk.Label(ventana)
etiqueta_resultado.pack()

ventana.mainloop()