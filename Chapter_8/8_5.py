def make_sandwitch(*ingredients):
    print("\nMaking a sandwitch with the following ingredients: ")
    for ingredient in ingredients:
            print(f" - {ingredient}")

make_sandwitch ("peanut butter" , "Jelly")
make_sandwitch("Pastrami" , "Sourkrout", "1000 Island Dressing")
make_sandwitch("Bacon" , "lettuce" , "tomato")

def build_profile(first , last , **user_info):
    user_info['First_name'] = first
    user_info['Last_name'] = last
    return user_info

user_profile = build_profile('Deven' , 'Perkins' ,location = 'San Diego' , field = 'film' , hobby = 'sailing')
print(f"\n {user_profile}")

def build_car(make , model , **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = build_car ('Toyota' , 'Marai' ,color = 'Nautical Blue' , tow_package = False)
print(f"\n {car}")