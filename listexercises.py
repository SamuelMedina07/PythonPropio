def separador():
    print('****************************************************************************')
""" 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
would you invite? Make a list that includes at least three people you’d like to 
invite to dinner. Then use your list to print a message to each person, inviting 
them to dinner."""

GuestsLastDinner = ['Pilar','Chini','Cindy','Julissa']
message = "estas cordialmente invitada a nuestra cena de fin año 2023 te esperamos"
print(f'{GuestsLastDinner[0]}',message)
print(f'{GuestsLastDinner[1]}',message)
print(f'{GuestsLastDinner[2]}',message)
print(f'{GuestsLastDinner[3]}',message)
print(f'Samuel you are inviting {len(GuestsLastDinner)} people to the party')
separador()
"""3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print() call at the end 
of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still 
in your list."""
print(f'Hello Samuel,I wont arrive to your party,with love {GuestsLastDinner[0]}')
del GuestsLastDinner[0]
GuestsLastDinner.append('Blanca')
print(f'{GuestsLastDinner[0]}',message)
print(f'{GuestsLastDinner[1]}',message)
print(f'{GuestsLastDinner[2]}',message)
print(f'{GuestsLastDinner[3]}',message)
separador()
"""3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger 
dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list. """
GuestsLastDinner.insert(0,'Sonia')
GuestsLastDinner.insert(3,'Rosa')
GuestsLastDinner.append('Nathalia')
print(f'{GuestsLastDinner[0]}',message)
print(f'{GuestsLastDinner[1]}',message)
print(f'{GuestsLastDinner[2]}',message)
print(f'{GuestsLastDinner[3]}',message)
print(f'{GuestsLastDinner[4]}',message)
print(f'{GuestsLastDinner[5]}',message)
print(f'{GuestsLastDinner[6]}',message)
separador()

"""3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two 
names remain in your list. Each time you pop a name from your list, print 
a message to that person letting them know you’re sorry you can’t invite 
them to dinner.
•	 Print a message to each of the two people still on your list, letting them 
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end 
of your program."""
print("I'm sorry, I can olny invite 2 people to the party my bad :(")
apologize_message="lo sentimos se canceló tu reservacion a la fiesta"
eliminar=GuestsLastDinner.pop(-1)
print(f'{eliminar}',apologize_message)
eliminar=GuestsLastDinner.pop(-1)
print(f'{eliminar}',apologize_message)
eliminar=GuestsLastDinner.pop(-1)
print(f'{eliminar}',apologize_message)
eliminar=GuestsLastDinner.pop(-1)
print(f'{eliminar}',apologize_message)
eliminar=GuestsLastDinner.pop(-1)
print(f'{eliminar}',apologize_message)
print(f'{GuestsLastDinner[0]}',message)
print(f'{GuestsLastDinner[1]}',message)
GuestsLastDinner.remove('Sonia')
GuestsLastDinner.remove('Chini')
print(f'Tu lista actual',GuestsLastDinner)