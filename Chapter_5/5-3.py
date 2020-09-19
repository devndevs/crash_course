user_names = ["admin" ,"dperkheezy" , "Nsyncbbgrl" , "ladyedarn" , "magasux"]

for user_name in user_names:
    if user_name == "admin":
        print(f"Hello admin, would you like a status report?")
    else:
        print(f"\nHello " +str(user_name) +", thank you for logging in again")

del user_names [0:]

if user_names:
    for user_name in user_names:
        print(f"\nHello " + str(user_name) + ", thank you for logging in again")
else:
    print("\nWe need to find more users!")

current_users = [ "dperkheezy" , "ladyedarn" , "wildangelslut22" , "magasux" , "rooluvmob"]
new_users = [ "catluver" , "$$$ball" , "wildangelslut22" , "magasux" , "poopsensitive"]

for new in new_users:
    if new in current_users:
        print(f"\nSorry, but the username" + str(new) + " is already taken")
    else:
        print(f"\nThe username " + str(new) + " is available")

numbers = range(1 , 10)

for num in numbers:
    if num == 1:
        print (f"\n" + str(num) + "st")
    elif num == 2:
        print (f"\n" + str(num) + "nd")
    elif num == 3:
        print (f"\n" + str(num) + "rd")
    else:
        print (f"\n" + str(num) + "th")
    
