""" 8-6. City Names: Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the 
values that are returned """

def city_country(city,country):
    Mundi={
        'city':city,
        'country':country
    }
    ret= f"'{Mundi['city'].title()},{Mundi['country'].title()}'"
    return ret

options = {
    'santiago':'chile',
    'tegucigalpa':'honduras',
    'berlin':'alemania'
}
for city,country in options.items():
    resp=city_country(city,country)
    print(resp)

""" 8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Use None to add an optional parameter to make_album() that allows you to 
store the number of songs on an album. If the calling line includes a value for 
the number of songs, add that value to the album’s dictionary. Make at least 
one new function call that includes the number of songs on an album """
def make_album(artist_name,artist_album,songs=None):
    Album = {
        'artist_album':artist_album,
        'artist_name':artist_name,
    }
    if songs:
        Album['songs']=songs

    return Album

new = make_album('bethel','we will not be shaken')
print(new)
new = make_album('hillsong','there is more',12)
print(new)
new = make_album('olivos verdes','gracia')
print(new)


""" 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created. Be sure to include a quit value in the while loop. """

def make_album(artist_name,artist_album,songs=None):
    Album = {
        'artist_album':artist_album,
        'artist_name':artist_name,
    }
    return Album

cont = True
while cont is True:
    alb=input("Hello! write the Album's Name...:")
    art=input("Hello! write the Artist's Name...:")
    print(make_album(art,alb))
    seguir =input("Type q to quit..>:")
    if seguir == 'q':
        cont=False
