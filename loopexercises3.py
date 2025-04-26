""" 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
•	 Print the message The first three items in the list are:. Then use a slice to 
print the first three items from that program’s list. """
Ingredientes_Camionero=['pan','bacon','queso cheddar','lechuga','tomate','carne de lenteja','pepinillos','salsas','cebolla']
print(f'The first three items of the list are:{Ingredientes_Camionero[:3]}')

""" •	 Print the message Three items from the middle of the list are:. Use a slice to 
print three items from the middle of the list. """
print(f'Three items form the middle of the list are:{Ingredientes_Camionero[3:6]}')

""" •	 Print the message The last three items in the list are:. Use a slice to print the 
last three items in the list. """
print(f'The last three items in the list are:{Ingredientes_Camionero[6:]}')


""" 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas. 
Then, do the following """
fav_pizzas=['pepperoni','mushroom','hawaiian']
friend_pizzas=fav_pizzas[:]

""" Add a new pizza to the original list. """
fav_pizzas.append('new yorker')

""" Add a different pizza to the list friend_pizzas. """
friend_pizzas.append('mini bite')

""" Prove that you have two separate lists. Print the message My favorite 
pizzas are:, and then use a for loop to print the first list. Print the message 
My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list. """
print('My favorite pizzas are:')
for mostrarMias in fav_pizzas[0:]:
    print(mostrarMias.title())

print("My friend's favorite pizzas are:")
for mostrarAmigos in friend_pizzas[0:]:
    print(mostrarAmigos.title())
    
#tuples =() son como listas pero no se pueden modificar 
La_Doña=('baleadas','pupusas')

for comida in La_Doña[0:]:
    print(comida)