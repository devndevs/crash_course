animals = [ "dog" , "cat", "raccoon" , "horse" , "snake" , "owl" , "turtle"]
print(f"The first three items on the list are:" , animals[:3])
print(f"\nThe middle three items on the list are:" , animals[2:5])
print(f"\nThe last three item on the list are:" , animals[3:])

pizza = [ "buffalo Chicken" , "sausage" , "hawaiian"]
friends_pizza = pizza[:]

pizza.append("veggie")
friends_pizza.append("cheese")

print("\nMy favorite pizzas are:")
for za in pizza:
    print(za)

print("\nMy friend's favorite pizzas are:")
for f_za in friends_pizza:
    print(f_za)

my_foods= ["pizza" , "falafel" , "carrot cake"]
friends_foods = my_foods[:]

my_foods.append("cheese cake")
friends_foods.append("french fries")
print()
for food in my_foods:
    print(food)
print()
for f_food in friends_foods:
    print(f_food)

        