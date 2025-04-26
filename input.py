"""7-1. Rental Car: Write a program that asks the user what kind of rental car they 
would like. Print a message about that car, such as “Let me see if I can find you 
a Subaru.”"""


def availablecars(car):
    cars = ["mustang","audi"]
    cars2= []
    while cars:
        carsTitle = cars.pop();
        cars2.append(carsTitle.title())
        
    if car not in cars2:
        existence = False
    else:
         existence = True
    return message(existence)

def message(existence):
    if existence is False:
        print(f"Oh sorry we dont have any {car} available at the moment")
    else:
        print(f"Yes we do have a {car} available")

car = input("Hello what kind of car would you like to rent: ")
car = car.title()
availablecars(car)




"""7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready."""

"""7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not"""

number = input("Type a number: ")
number = int(number)
divisible = 10

if number % divisible:
    print(f"Not Divisible by {divisible}")
else:
    print(f"Divisible by {divisible}")