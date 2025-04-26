requested_toppings =['mushrooms','green peppers','extra chesse']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print ("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("Finished making your pizza!\n")

#si el nombre de un arreglo esta en un if evalua si esta vacio(false) o lleno(true)
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")
    

available_toppings=('mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese')

requested_toppings2=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings2:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f'Sorry, we dont have {requested_topping}')
print(f'Pizza finished')
    