def city_country (city, country):
    citry = f"{city} , {country}"
    return citry

solution = city_country("Washington D.C." , "USA")
print (solution)
print (city_country("Amsterdam" , "Netherlands"))
print (city_country("Sydney" , "Australia"))
print (city_country("Tokyo" , "Japan"))

print()

def make_album(artist, title , songs = None):
    album = {'Artist' : artist , 'Song' : title}
    if songs:
        album['songs'] = songs
    return album

print(make_album("alt J" , "An Awesome Wave"))
print(make_album("Brand New" , "Deja Entendu" , "10"))
print(make_album("Nirvana" , "Bleach" , "9"))

