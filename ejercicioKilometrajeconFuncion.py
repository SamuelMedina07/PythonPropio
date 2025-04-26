def CalcKilometers (ActualKilometer,Fabricationyear):
    Actualyear=2025
    global Years 
    Years = Actualyear - Fabricationyear
    KMmedia = ActualKilometer / (Years)
    return (KMmedia)
data = {
    'Crossfox': {'km': 35000, 'año': 2005}, 
    'DS5': {'km': 17000, 'año': 2015}, 
    'Fusca': {'km': 130000, 'año': 1979}, 
    'Jetta': {'km': 56000, 'año': 2011}, 
    'Passat': {'km': 62000, 'año': 1999}
}


def km_media(dataset, año_actual):
    for item in dataset.items():
        result = item[1]['km'] / (año_actual - item[1]['año'])
       # print(result)
km_media(data, 2025)


for car,carsinfo in data.items(): 
    ActualKilometer = carsinfo['km']
    Fabricationyear = carsinfo['año']
    CalculoKilometrajePromedio = CalcKilometers (ActualKilometer,Fabricationyear)
    print(car.title())
    print(f"\tKilometraje actual es:{ActualKilometer}")
    print(f"\tAño de fabricacion:{Fabricationyear}")
    print(f"\tEdad:{Years}")
    print("\tKilometraje por año:{:.2f}".format(CalculoKilometrajePromedio))
       