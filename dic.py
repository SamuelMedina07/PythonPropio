chini={
        'first_name':'chini',
        'middle_name':'suyapa',
        'last_name':'ramirez',
        'mother_name':'varela',
        'age':49,
        'birthplace':'tegucigalpa',
        'grade':'preparatory'
    }

samuel={
        'first_name':'samuel',
        'middle_name':'ernesto',
        'last_name':'medina',
        'mother_name':'ramirez',
        'age':24,
        'birthplace':'san pedro sula',
        'grade':'university'
        }

oso={  
    'first_name':'oso',
        'middle_name':'papa',
        'last_name':'ramirez',
        'mother_name':'jugetona',
        'age':2,
        'birthplace':'san pedro sula',
        'grade':'kinder'
     }

def fullname(first_nam,last_nam):
    full= first_nam+ "\t" +last_nam;
    return full;

def grade(grad):
    courses=['Kinder','Preparatory','College'];
    if grad not in courses:
        return 'N/A';
    else:
        return grad; 


def datapresetation():
    pres ='NAME'+'\tLAST NAME'+'\tACADEMIC HISTORY';
    return pres;
    


print(datapresetation());
people=[chini,oso,samuel]
for person in people:
    first_nam=person['first_name'].title();
    last_nam=person['last_name'].title();
    grad=person['grade'].title();
    print(fullname(first_nam,last_nam),'\t',grade(grad),'\n');
