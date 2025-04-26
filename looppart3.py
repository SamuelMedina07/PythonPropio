#slice [0:3] indica desde cual indice hasta donde terminar
players=['charles','martina','michael','florence','eli']
print(players[0:3]) #o print(players[:3])
#desde el ultimo hasta el inidicado
print(players[2:])
#desde el ultimo hasta el primero con 1 espacio de por medio
print(players[0::2])
#verificando si esta la cantidad de jugadores existe y si existe un for en una lista hasta un indice determinado
cant=int(input('Ingrese la cantidad de jugadores que desea ver..:'))
if cant>len(players):
    print(f'Error usted solo tiene {len(players)} de jugadores')
    
else:
    print(f'Here are the first {cant} players on my team:')
    for player in players[:cant]:
        print(player.title())

#copiando una lista exactamente igual [:] hasta el ultimo elemento acutal
my_food=['pizza','falafel','carrot cake']
chinis_food=my_food[:]


