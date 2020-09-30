prompt = "\n Please let us know what toppings you'd like on your pizza!"
prompt += "\n Once finished please enter 'done' to complete order "

while True:
    toppings = input(prompt)
    
    if toppings == 'done':
        break
    else:
        print(f"Adding {toppings.title()} to your delicious pizza")


prompt = "\n Please enter the age of who the movie ticket will be for"
age = int(age)

active = True

while True:
    if age == "done":
        active = False
    elif age < 3:
        print (f"\nYour child can get in for free")
        print (f"\nIf you are finished buying tickets, please enter 'done'")
        break
    elif age >= 3 and age <= 12:
        print(f"\nIt will cost $12 for your child's ticket")
        print (f"\nIf you are finished buying tickets, please enter 'done'")
    elif age > 12:
        print (f"\n The cost of this ticket is $15")
        print (f"\nIf you are finished buying tickets, please enter 'done'")
        break
    else:
        break
