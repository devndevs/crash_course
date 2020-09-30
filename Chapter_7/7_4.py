sando_orders = ["italian" ,"pastrami" , "chicken" , "turkey" , "ruben" , "pastrami" , "peanut butter and jelly" , "pastrami"]
finished_sando = []

while "pastrami" in sando_orders:
    sando_orders.remove("pastrami")

print(f"\nThe Deli has run out of pastrami.")
        
while sando_orders:
    making_sando = sando_orders.pop()

    print(f"\nI made your {making_sando.title()} sandwitch")
    finished_sando.append(making_sando)

print(f"\nThe following sandwitches were made:")
for sando in finished_sando:
    print(f"\n{sando.title()}")

