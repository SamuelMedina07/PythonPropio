""" 6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, and the city in which they live. You 
should have keys such as first_name, last_name, age, and city. Print each 
piece of information stored in your dictionary. """
mother={
    'first_name':'chini',
    'last_name':'ramirez',
    'city':'tegucigalpa'
}

print(f'My moms name is {mother['first_name'].title()} and last name is {mother['last_name'].title()} she born in {mother['city'].title()}')

""" 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program. """

favorite_numbers={
    'samuel':5,
    'chini':1,
    'paty':7,
    'ariela':10,
    'alex':9
}

print(f'Samuels favorite number is {favorite_numbers['samuel']}')
print(f'Chinis favorite number is {favorite_numbers['chini']}')
print(f'Patys favorite number is {favorite_numbers['paty']}')
print(f'Arielas favorite number is {favorite_numbers['ariela']}')
print(f'Alexs favorite number is {favorite_numbers['alex']}')

