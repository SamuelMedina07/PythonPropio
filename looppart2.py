#range (1,5) muestra desde 1 en pantalla pero empieza desde posicion 0 
for number in range(1,5):
    print(number)
#range (5) muestra desde 0 en pantalla empieza desde posicion 0 
for number2 in range(5):
    print(number2)
#en un array guarda numeros con un ciclo for list(range()) 
numeros=list(range(1,6))
print(numeros)
#en un array guarda numeros de 2 en 2 con un ciclo for list(range(2,11,2)) 
numeros_pares = list(range(2,11,2))
print(numeros_pares)
#se representa un exponente **, mostrando el cuadrado de los primeros 10 numeros
squares=[]
for numero in range(1,11):
    #square es un variable temporal por cada ciclo lo eleva a la potencia 2 luego esa variable temporal la almacena en el array squares
    """ square=numero**2
    squares.append(square)
    print(f'{numero}^2={square}') """
    squares.append(numero**2) 
print(squares)   
#list comprehensions combina el for y los elementos los agrega segun como va el ciclo
numeros_cuadrados=[numero**2 for numero in range(1,11)]
print(numeros_cuadrados)
#min() el numero minimo de la lista
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
#max() el numero maximo de la lista
print(max(digits))
#sum() suma todos los numeros de la lista
print(sum(digits))
