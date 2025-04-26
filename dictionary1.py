alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points= alien_0['points']
print(f'You just earned {new_points} points!')

#añadiendo al diccionario de alien_0
alien_0['x_position']=0
alien_0['y_position']=25

print(alien_0)

#creando un diccionario vacio y luego llenandolo

alien_1={}

alien_1['color'] ='red'
alien_1['points']=10
print(alien_1)

""" For a more interesting example, lets track the position of an alien that 
can move at different speeds. Well store a value representing the aliens 
current speed and then use it to determine how far to the right the alien 
should move: """

alien_3={'x_position':0,'y_position':25,'speed':'medium'}
print(f"The original position: {alien_3["x_position"]}")

if alien_3['speed']=='slow':
    x_increment=1
elif alien_3['speed']=='medium':
    x_increment=2
else:
    x_increment=3
    
# The new position is the old position plus the increment.
alien_3['x_position'] += x_increment

print(f'New position: {alien_3["x_position"]}')

#removiendo una llave dentro de un diccionario
#del alien_0['points']


""" The previous example involved storing different kinds of information about 
one object, an alien in a game. You can also use a dictionary to store one 
kind of information about many objects. For example, say you want to poll a 
number of people and ask them what their favorite programming language 
is. A dictionary is useful for storing the results of a simple poll, like this: """

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

language=favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")