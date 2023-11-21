import requests


def obtener_partidos():
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
