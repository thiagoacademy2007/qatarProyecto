import requests
import random

def obtener_partidos_random():
    # Obtén todos los partidos de la Copa del Mundo
    respuesta = requests.get("https://worldcupjson.net/matches/")
    
    if respuesta.status_code == 200:
        partidos = respuesta.json()
        
        # Selecciona un partido aleatorio
        partido_aleatorio = random.choice(partidos)
        
        # Extrae información relevante del partido
        equipo_local = partido_aleatorio["home_team"]["country"]
        equipo_visitante = partido_aleatorio["away_team"]["country"]
        goles_local = partido_aleatorio["home_team"]["goals"]
        goles_visitante = partido_aleatorio["away_team"]["goals"]
        
        resultado_partido = {
            "Equipo Local": equipo_local,
            "Equipo Visitante": equipo_visitante,
            "Goles Equipo Local": goles_local,
            "Goles Equipo Visitante": goles_visitante
        }
        
        return resultado_partido
    else:
        print("Error al obtener los partidos de la Copa del Mundo")
        return None

# Ejemplo de cómo usar la función
partido_aleatorio = obtener_partidos_random()
if partido_aleatorio:
    print("Partido Aleatorio:")
    for clave, valor in partido_aleatorio.items():
        print(f"{clave}: {valor}")
