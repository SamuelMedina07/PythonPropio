""" 5-8. Hello Admin: Make a list of five or more usernames, including the name 
'admin'. Imagine you are writing code that will print a greeting to each user 
after they log in to a website. Loop through the list, and print a greeting to 
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin, 
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for 
logging in again.
•   If the list is empty, print the message We need to find some users!"""

users=['admin','samuel','chini','cindy','julissa']

if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user} thank you for logging in again')
else:
    print(f'We have {len(users)} users need to find some users')
    
    
""" 5-10. Checking Usernames: Do the following to create a program that simulates 
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or 
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already 
been used. If it has, print a message that the person will need to enter a 
new username. If a username has not been used, print a message saying 
that the username is available."""

current_users=['nelson','samuel','chini','cindy','julissa']
new_users=['carlos','samuel','chini','rony','velez']


for new_user in new_users:
    if new_user not in current_users:
        print(f'The user:{new_user} is available')
    else:
        print(f'Sorry, {new_user} is already taken')
        

""" 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 
7th 8th 9th", and each result should be on a separate line. """

ORDINALS_NUMBERS=[1,2,3,4,5,6,7,8,9]

for ordinal_number in ORDINALS_NUMBERS:
    if ordinal_number == 1:
        print(f'{ordinal_number}st')
    elif ordinal_number == 2:
        print(f'{ordinal_number}nd')
    elif ordinal_number== 3:
        print(f'{ordinal_number}rd')
    else:
         print(f'{ordinal_number}th')
