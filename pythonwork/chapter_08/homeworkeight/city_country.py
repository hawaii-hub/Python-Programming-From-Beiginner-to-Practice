def city_country(city, country):
    """"""
    city_name = f"{city} {country}"
    return city_name.title()

name = city_country('santiago', 'chile')
print(name)

#专辑

def make_album(name, music, number=None):
    """"""
    dictionary = {'first': name, 'last': music}
    if number:
        dictionary['number'] = number
    return dictionary

#用户的专辑

while True:
    print("\nPlease int name and album")

    name = input("musician_name:")
    if name == 'q':
        break

    music = input("music:")

    album = make_album(name, music)
    print(album)
