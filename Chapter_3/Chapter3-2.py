guest_list= ["Marcus Aurelius" , "Martin Luther King Jr." , "George Carlin"]

print("Greetings,",guest_list[0],", I would be honored if you could join my other destinguised guests to dinner with me\n")
print("Greetings,",guest_list[1],", I would be honored if you could join my other destinguised guests to dinner with me\n")
print("Greetings,",guest_list[2],", I would be honored if you could join my other destinguised guests to dinner with me\n")

guest_list[0] = "Richard Branson"

print("Greetings,",guest_list[0],", I would be honored if you could join my other destinguised guests to dinner with me\n")
print("Greetings,",guest_list[1],", I would be honored if you could join my other destinguised guests to dinner with me\n")
print("Greetings,",guest_list[2],", I would be honored if you could join my other destinguised guests to dinner with me\n")
print("Attention, We have found a bigger table, please keep your eyes peeled for another invitation coming soon\n")

guest_list.insert(0 ,"Rosa Parks")
guest_list.insert(2, "Robin Williams")
guest_list.append("Abraham Lincoln")

print(f"Greetings, " + str(guest_list[0]) + ", I would be honored if you could join my other destinguised guests to dinner with me.\n")
print(f"Greetings, "+ str(guest_list[1]) +", I would be honored if you could join my other destinguised guests to dinner with me.\n")
print(f"Greetings, "+ str(guest_list[2]) +", I would be honored if you could join my other destinguised guests to dinner with me.\n")
print(f"Greetings, "+ str(guest_list[3]) +", I would be honored if you could join my other destinguised guests to dinner with me.\n")
print(f"Greetings, "+ str(guest_list[4]) +", I would be honored if you could join my other destinguised guests to dinner with me.\n")
print(f"Greetings, "+ str(guest_list[5]) +", I would be honored if you could join my other destinguised guests to dinner with me.\n")

print("Due to the table shortage I will now only be allowed to invite two guests. This breaks by heart to have to choose from such wonderful people.\n")

print("It's with my deepest apologies that I have to inform you, " +str(guest_list.pop(1)) + ", that I will no longer have room to invite you.\n")
print("It's with my deepest apologies that I have to inform you, " +str(guest_list.pop(1)) + ", that I will no longer have room to invite you.\n")
print("It's with my deepest apologies that I have to inform you, " +str(guest_list.pop(1)) + ", that I will no longer have room to invite you.\n")
print("It's with my deepest apologies that I have to inform you, " +str(guest_list.pop(1)) + ", that I will no longer have room to invite you.\n")
print("It brings me great joy that I can still invite you, " + str(guest_list[0]) + ", to the dinner of a lifetime.\n" ) 
print("It brings me great joy that I can still invite you, " + str(guest_list[1]) + ", to the dinner of a lifetime.\n" ) 

del guest_list[0]
del guest_list[0]