responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("\nIf you could travel anywhere in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no)  ")

    if repeat == 'no':
        polling_active = False

print ("---Poll Results---")
for name, response in responses.items():
    print(f"\n{name} would like to travel to {response}")