bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# el negativo indica desde el ultimo -1 , -2 penultimo etc..
print(bicycles[-1].upper())

# append añade un elemento al final de la lista
bicycles.append('ducati')
# insert(0) añade un elemento a la lista y el numero indica su posicion
bicycles.insert(0,'honda')
# del elimina cualquier elemento segun la posicion
del bicycles[-1]
#remove elimina del arreglo pero con texto
bicycles.remove('redline')
#pop elimina del arreglo pero lo guarda en memoria para usarlo luego
first_bicycle = bicycles.pop(0)
print(f'My first bycicle was {first_bicycle}')
print(bicycles)
