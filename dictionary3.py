#nesting guardar un diccionario dentro de una lista o viceversa

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
    
    
#ejercicio creando una flota de 30 aliens verdes

aliens=[]
#creando y almacenando en aliens 30 alien verdes 
for alien_number in range(30):
    new_alien={'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
#alterando los primeros 3 alien con otro color,puntos y velocidad
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
        
#imprimiendo los primeros 5 alien dentro del arreglo aliens  
for alien in aliens[:5]:
    print(alien)
print("...")
#ver el total de alien dentro del arreglo aliens
print(f'Total number of aliens: {len(aliens)}')



#guardando una lista dentro de un diccionario 

pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print(f'You ordered a {pizza['crust']}-crust pizza '
      'with the following with the following toppings:')

for topping in pizza['toppings']:
    print('\t',topping)
    
    
#mejorando lenguajes de programacion

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
verbs =('are','is')
for name, languages in favorite_languages.items():
    
    if len(languages) != 1:
        verb=verbs[0]
    else:
        verb=verbs[1]
        
    print(f"\n{name.title()}'s favorite languages {verb}:")
    for language in languages:
        print(f"\t{language.title()}")


#diccionario para guardar informacion de los usuarios de una pagina web

user= {
    'aeisntein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username,user_info in user.items():
    print(f'User name:{username}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f'Full name:{full_name.title()}')
    print(f'Location:{location.title()}\n')
    
