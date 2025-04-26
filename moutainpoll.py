""" Filling a Dictionary with User Input
You can prompt for as much input as you need in each pass through a while
loop. Let’s make a polling program in which each pass through the loop 
prompts for the participant’s name and response. We’ll store the data we 
gather in a dictionary, because we want to connect each response with a 
particular user
 """
responses = {}

polling_active = True

while polling_active:
    name= input("What is your name? ")
    reponse = input("Which mountain would you like to clime someday? ")
    responses[name]=reponse
    repeat=input("Would you like to let another person respond? (yes/no)")

    if repeat == 'no':
        polling_active = not True


print("\n --- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")