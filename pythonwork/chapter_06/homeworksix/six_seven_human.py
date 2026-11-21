# 6.7 人们：
    # #在6.1程序中

# 6.8 宠物
旺财 = {
    'animal': 'dog', 
    'owner': 'alice'
}

咪咪 = {
    'animal': 'cat',
    'owner': 'bob'
}

小金 = {
    'animal': 'fish',
    'owner': 'chaelie'
}

pets = [旺财,咪咪,小金]

for pet in pets:
    print(pet)

# 6.9 喜欢的地方
print('')

favorite_places = {
    'liujingrui':['tokyo', 'seoul', 'bangkok'],
    'lishan':['singapore', 'dubai', 'paris'],
    'honghong':['london', 'rome', 'berlin']
}

for name,places in favorite_places.items():
    print(f"\n{name}likes:")
    for place in places:
        print(f" -{place}")

# 6.11 城市
print()

cities = {
    'beijing': {
        'country': 'china',
        'population': 2171_0000,
        'face': "It's the capital in china.",
    },

    'tokyo': {
        'country': 'japan',
        'popilation': 1396_0000,
        'fact': "It's one of the most populous cities in the world.",
    },
    
    'paris': {
    'country': 'france',
    'population': 216_0000,
    'fact': "It's known as the City of Light.",
    }
    
}

print(cities)