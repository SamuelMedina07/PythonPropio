#lista de usuarios banneados, not in
banned_users=['loli','porky']
user=input('Ingrese su usuario..:')
if user not in banned_users:
    print(f'Hello {user} welcome back!')
else:
    print(f'{user} estas baneado por 5 dias')
    
    
#verificando si hay algun ingrediente disponible, in 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

#amusement park, if elif else es un blockchain

edad=int(input('Ingrese su edad..:'))
if edad<=4:
    precio=0
elif edad <=18:
    precio=25
else:
    precio=40
print(f'Para su edad de {edad} años debe pagar la cantidad de ${precio}')    

 