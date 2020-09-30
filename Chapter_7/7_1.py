car = input(f"What kind of car are you looking for: ")
print(f"\nI see you are looking for a {car}")

people = input(f"How many people are in your dinner group? ")
people = int(people)

if people <= 8:
    print(f"\nYour table is ready")
else:
    print("You'll have to wait for a table")

number = input("Enter a number and I will tell you if its devisable by 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is devisable by 10")
else:
    print(f"\nThe number {number} is NOT devisable by 10")

