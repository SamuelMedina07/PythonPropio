""" 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). 
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person. """
chini={
        'first_name':'chini',
        'middle_name':'suyapa',
        'last_name':'ramirez',
        'mother_name':'varela',
        'age':49,
        'birthplace':'tegucigalpa'
    }

    
samuel={
        'first_name':'samuel',
        'middle_name':'ernesto',
        'last_name':'medina',
        'mother_name':'ramirez',
        'age':23,
        'birthplace':'san pedro sula'
        }

oso={  
    'first_name':'oso',
        'middle_name':'papa',
        'last_name':'ramirez',
        'mother_name':'jugeton',
        'age':2,
        'birthplace':'san pedro sula'
     }

people=[chini,samuel,oso]
for person in people:
    print(person,'\n')
    
""" 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person.Loop through the dictionary, and print 
each person’s name and their favorite places. """


favorite_places={
    'samuel':['san pedro sula','panama','cancun'],
    'chini':['tegucigalpa'],
    'pilar':['tegucigalpa','olancho']
}
def grammar(places):
    if len(places) != 1:
        verb='places are'
    else:
        verb='place is'
    return(verb)
    
for friend,places in favorite_places.items():
    print(f'\n{friend.title()} favorite {grammar(places)}:')
    for place in places:
        print(f'{place.title()}')
        
        
""" 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) 
so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers. """

favorite_numbers={
    'samuel':[2,1],
    'chini':[5,9],
    'paty':[7,99],
    'ariela':[100,34],
    'alex':[1,5]
}

for participant, numbers in favorite_numbers.items():
    print(f'\n{participant.title()}´s favorite numbers are:')
    for number in numbers:
        print(number)
        
""" 6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
keys in your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the information you have stored about it """

cities={
    'san pedro sula':{
        'country':'Honduras',
        'population':1_000_000,
        'fact':'City where Samuel Ernesto Medina Ramirez was born'
    },
    'tegucigalpa':{
        'country':'Honduras',
        'population':1_800_000,
        'fact':'City where Chini Suyapara Ramirez Varela was born'
    },
    'capital':{
        'country':'Norway',
        'population':3_000_000,
        'fact':'City where Magnus Carlsen was born'
    }
    
}

for city,citiesinfo in cities.items():
    print(city.title())
    for cityinfo,description in citiesinfo.items():
        print(f"\t{cityinfo.title()}:{description}")
    