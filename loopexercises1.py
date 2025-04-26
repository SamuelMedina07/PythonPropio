""" 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
pizza names in a list, and then use a for loop to print the name of each pizza. """
fav_pizzas=['pepperoni','mushroom','hawaiian']
for pizza in fav_pizzas:
    print(pizza)
    
""" •	 Modify your for loop to print a sentence using the name of the pizza 
instead of printing just the name of the pizza. For each pizza you should 
have one line of output containing a simple statement like I like pepperoni 
pizza. """
for pizza in fav_pizzas:
    print(f"Hello I'am Samuel and I like {pizza} pizza")
    
""" •	 Add a line at the end of your program, outside the for loop, that states 
how much you like pizza. The output should consist of three or more lines 
about the kinds of pizza you like and then an additional sentence, such as 
I really love pizza! """
print('I really love pizza')

""" 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal. """
farm_animals=['pig','cow','chicken']
for animal in farm_animals:
    print(animal)

""" •	 Modify your program to print a statement about each animal, such as 
A dog would make a great pet. """
for animal in farm_animals:
    print(f'The {animal} is a eatable animmal jummy')
    
""" •	 Add a line at the end of your program stating what these animals have in 
common. You could print a sentence such as Any of these animals would 
make a great pet! """
print('Any of these animals are delicious to be eaten')