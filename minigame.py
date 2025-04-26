import random as rc

paises = [
    ["nicaragua","managua"],
    ["honduras","tegucigalpa"]
]
jugando = True;

while jugando:
    opciones = len(paises)-1
    pais = rc.randint(0,opciones)
    capital = paises[pais][1]
    respuesta = input(f"Cual es la capital de {paises[pais][0].capitalize()}:") 
    if respuesta != capital:
        jugando = not jugando;
        print("malo pibe")
    else:
        print("bueno")

