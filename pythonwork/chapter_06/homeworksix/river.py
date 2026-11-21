# 6.5 river

rivers ={
    'nile': 'egypt',
    'amazon': 'brazi',
    'yangtze': 'china',
}

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

# 打印河流
print("\nRivers:")

for river in rivers.keys():
    print(river)

# 打印国家
print('\nCountrys:')

for country in rivers.values():
    print(country)