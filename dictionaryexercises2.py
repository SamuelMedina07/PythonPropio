""" 6-5. Rivers: Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary """


rivers={
    'nile':'egypt',
    'choluteca':'honduras',
    'amazonas':'brazil'
}

for river,country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')
    
for r in rivers.keys():
    print(r.title())
    
for c in rivers.values():
    print(c.title())
    
""" 6-6. Polling: Use the code in favorite_languages.py (page 97).
•	 Make a list of people who should take the favorite languages poll. Include 
some names that are already in the dictionary and some that are not. 
•	 Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding. 
If they have not yet taken the poll, print a message inviting them to take 
the poll. """

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

invitation_message="we invite you to complete the poll"
thank_you_message="thank you for responding the poll"

people=['samuel','chini','jen','dora','laura','phil']

for person in people:
    if person not in favorite_languages.keys():
        print(person.title(),invitation_message)
    else:
        print(f'Hello',person.title(),thank_you_message)
       