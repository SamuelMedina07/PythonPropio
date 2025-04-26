unprinted_models = ['phone case','robot pendant','dodecahedron']
printed_models=[]


while unprinted_models:
    current_design = unprinted_models.pop()
    print(f'Printing model...: {current_design.title()}')
    printed_models.append(current_design)

print('The following models have been printed:')

for completed_model in printed_models:
    print(completed_model)