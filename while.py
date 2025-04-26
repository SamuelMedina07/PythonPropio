""" 7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket 
Use a break statement to exit the loop when the user enters a 'quit' value """
def price(age):
    age = int(age)
    if age <3:
        print("Free ticket")
    elif age <= 12:
        print("$10")
    elif age > 12:
        print("$15")

people = True 
while people is True:
    age = input("Age: ")
    if age != "quit":
        price(age)
    else:
        break
    