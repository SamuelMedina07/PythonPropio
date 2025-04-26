""" 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•	 Write an if statement to test whether the alien’s color is green. If it is, print 
a message that the player just earned 5 points.
•	 Write one version of this program that passes the if test and another that 
fails. (The version that fails will have no output.) """

alien_color='red'
if 'green' in alien_color:
    print('Just earned 5 points')
if 'red' in alien_color:
    print()
    
""" 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
write an if-else chain.
•	 If the alien’s color is green, print a statement that the player just earned 
5 points for shooting the alien.
•	 If the alien’s color isn’t green, print a statement that the player just earned 
10 points.
•	 Write one version of this program that runs the if block and another that 
runs the else block. """
if (alien_color!='green'):
    print('Just earned 10 points')
else:
    print('Just earned 5 points')

""" 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
•	 If the alien is green, print a message that the player earned 5 points.
•	 If the alien is yellow, print a message that the player earned 10 points.
•	 If the alien is red, print a message that the player earned 15 points.
•	 Write three versions of this program, making sure each message is printed 
for the appropriate color alien. """

if (alien_color=='green'):
    points=5
elif (alien_color=='yellow'):
    points=10
else:
    points=15
print(f'Just earned {points} points in {alien_color} alien')


""" 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
stage of life. Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is 
a baby.
•	 If the person is at least 2 years old but less than 4, print a message that 
the person is a toddler.
•	 If the person is at least 4 years old but less than 13, print a message that 
the person is a kid.
•	 If the person is at least 13 years old but less than 20, print a message that 
the person is a teenager.
•	 If the person is at least 20 years old but less than 65, print a message that 
the person is an adult.
•	 If the person is age 65 or older, print a message that the person is an 
elder. """
person_age=0
if person_age<2:
    StageOfLife='baby'
elif person_age<4:
    StageOfLife='toddler'
elif person_age<13:
    StageOfLife='kid'
elif person_age<20:
    StageOfLife='teenager'
elif person_age<65:
    StageOfLife='adult'
else:
    StageOfLife='elder'
print(f'Your age is {person_age} and you are consider as a {StageOfLife}')

""" 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
independent if statements that check for certain fruits in your list.
•	 Make a list of your three favorite fruits and call it favorite_fruits.
•	 Write five if statements. Each should check whether a certain kind of fruit 
is in your list. If the fruit is in your list, the if block should print a statement, 
such as You really like bananas! """

favorite_fruits =['bananas','cherry','apple']
requested_fruit=input("Lets see if we got the fruit..:")
if requested_fruit not in favorite_fruits:
    print(f'Sorry we dont have {requested_fruit}')
else:
    print(f'Yummy we have {requested_fruit}')