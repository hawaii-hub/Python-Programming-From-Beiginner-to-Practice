def make_car(make, model, **toppings):
    """"""
    toppings['make'] = make
    toppings['model'] = model
    return toppings

car = make_car('subaru', 'outback', color='bule', tow_package='Ture')

print(car)