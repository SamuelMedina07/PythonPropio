user_0={
    'username':'smedina',
    'first':'samuel',
    'last':'medina'
}
#ciclo for con dos varibles para ver la key y el valor que tiene esa llave dentro de ese diccionario ,metodo items() es lo que contiene el diccionario 
for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
    
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}")
    

#metodo .key() ve las llaves del diccionario
for name in favorite_languages.keys():
 print(name.title())


"""  You can access the value associated with any key you care about inside 
the loop by using the current key. Let’s print a message to a couple of friends 
about the languages they chose. We’ll loop through the names in the dictionary as we did previously, but when the name matches one of our friends, we’ll 
display a message about their favorite language: """
print('\n')
friends=['phil','sarah']
for friend in favorite_languages.keys():
    if friend in friends:
        language = favorite_languages[friend].title()
        print(f"{friend.title()} you like {language}")
        
        
#primero ordenando llaves y luego mostrando 
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll')
    

#metodo .value() ve los valores del diccionario
print("The following languages have been mentioned without repeating:")
for language in favorite_languages.values():
    print(f'{language.title()}')


#metodo .value() ve los valores del diccionario y set() solo permite un item unico es decir que no repite un item solo muestra 1 
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f'{language.title()}')
    
    
#el set() tambien puede ser interpretado en dentro {}
aguas={'arroyo','aguazul','aguazul'}
print(aguas)
