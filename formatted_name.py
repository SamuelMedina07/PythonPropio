def get_formatted_name(first_name,last_name,middle_name=''):

    if not middle_name:
        full_name = f'{first_name} {last_name}'
    else:
        full_name = f'{first_name} {middle_name} {last_name}' 
    return full_name

musician = get_formatted_name('Samuel','Medina')
print(musician)
musician=get_formatted_name('Samuel','Medina','Ernesto')
print(musician)