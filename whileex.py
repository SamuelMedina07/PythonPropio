""" 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order, such 
as I made your tuna sandwich. As each sandwich is made, move it to the list 
of finished sandwiches. After all the sandwiches have been made, print a 
message listing each sandwich that was made. """

sandwich_orders = ['BLT','Club','Grilled Cheese','Reuben','Turkey Avocado','Chicken Salad','Philly Cheesesteak','Caprese','Pulled Pork','Egg Salad','Pastrami','Pastrami','Pastrami']
pending_sandwiches =[]
finished_sandwiches = []


res = True
while res is True:
    res = input('NOT SELLING TODAY:')
    if(res=='NULL'):
        break
    else:
        pending_sandwiches.append(res)
        res = True


print('We are very sorry but we are out of pastrami\n')
while 'Pastrami' in sandwich_orders:
    pending_sandwiches.append('Pastrami')
    sandwich_orders.pop()
    

while sandwich_orders:
    sandwichORDER = sandwich_orders.pop(0) 
    finished_sandwiches.append(sandwichORDER)
    print(f'{sandwichORDER} sandwich is already finished')
    
print("\nThe sandwiches that were made during the day",','.join(finished_sandwiches))
print(f"Pending sandwiches {pending_sandwiches}")
