import tkinter as tk
from tkinter import ttk

Paises = [
     "QAT: Qatar",
    "ECU: Ecuador",
    "SEN: Senegal",
    "NLD: Países Bajos",
    "ENG: Inglaterra",
    "IRN: Irán",
    "USA: Estados Unidos",
    "WAL: Gales",
    "ARG: Argentina",
    "KSA: Arabia Saudita",
    "MEX: México",
    "POL: Polonia",
    "FRA: Francia",
    "AUS: Australia",
    "DIN: Dinamarca",
    "TUN: Túnez",
    "ESP: España",
    "CR: Costa Rica",
    "GER: Alemania",
    "JPN: Japón",
    "BEL: Bélgica",
    "CAN: Canadá",
    "MAR: Marruecos",
    "HR: Croacia",
    "BRA: Brasil",
    "SRB: Serbia",
    "SUI: Suiza",
    "CM: Camerún",
    "POR: Portugal",
    "GHA: Ghana",
    "URY: Uruguay",
    "KOR: Corea Del Sur"
]

def treeview():
    ventana = tk.Tk()
    ventana.title("Equipos del Mundial")
    ventana.geometry("400x1000")

    tabla = ttk.Treeview(ventana, columns=("Paises",), height=70)  # Puedes ajustar la altura según tus necesidades
    tabla.heading("Paises", text="Paises")
    tabla.grid()

    for pais in Paises:
        tabla.insert("", "end", values=(pais,))

    ventana.mainloop()

treeview()
