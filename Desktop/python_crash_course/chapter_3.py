# 3-1

# storing friends in a list
friends = ["Ken" , "Ralph" , "John" , "Danny"]

#print each one of their names by calling them by thier index
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# 3-2

print(f"It's good to see you, {friends[0]}.")
print(f"It's good to see you, {friends[1]}.")
print(f"It's good to see you, {friends[2]}.")
print(f"It's good to see you, {friends[3]}.")

# 3-3

transportation= ["motorcycle" , "hydrogen car" , "bicycle" , "Birds"]

print(f"The first vehicle I owned in California was a Honda {transportation[0]}.")
print(f"The current car I own is a {transportation[1]}, made by Toyota.")
print(f"I rode my{transportation[2]} across America in 2015.")
print(f"Sometimes Erin and I like to ride {transportation[3]} to the zoo.")

# 3-4

guest_list=[ "Alexander Hamilton" , "Thom Yorke" , "Martin Luther King Jr."]

print(f"Hello {guest_list[0]}, I would like to invite you to dinner")
print(f"Hello {guest_list[1]}, I would like to invite you to dinner")
print(f"Hello {guest_list[2]}, I would like to invite you to dinner")

# 3-5 

print(f"It looks like {guest_list[1]} will not be able to make it to dinner.")

guest_list[1]= "Ghandi"

print(f"Hello {guest_list[0]}, I would like to invite you to dinner")
print(f"Hello {guest_list[1]}, I would like to invite you to dinner")
print(f"Hello {guest_list[2]}, I would like to invite you to dinner")

# 3-6 

print("It looks liek we were able to find a bigger table so I will be able to invite more people")

guest_list.insert(0, "Amelia Earhardt")
guest_list.insert(2, "Ann Frank")
guest_list.append("Marcus Areulious")

print(f"Hello {guest_list[0]}, I would like to invite you to dinner")
print(f"Hello {guest_list[1]}, I would like to invite you to dinner")
print(f"Hello {guest_list[2]}, I would like to invite you to dinner")
print(f"Hello {guest_list[3]}, I would like to invite you to dinner")
print(f"Hello {guest_list[4]}, I would like to invite you to dinner")
print(f"Hello {guest_list[5]}, I would like to invite you to dinner")

# 3-7 

print("Sorry, not the greatest news but the promised amount of tables will not be delivered and now I can only have two guests.")

print(guest_list)

removed_guest = guest_list.pop(1)

print(f"I'm sorry {removed_guest}, but due to the new table situation I will need to uninvite you, hope to catch you at the next dinner")

removed_guest = guest_list.pop(4)

print(f"I'm sorry {removed_guest}, but due to the new table situation I will need to uninvite you, hope to catch you at the next dinner")

print(guest_list)

removed_guest = guest_list.pop(0)

print(f"I'm sorry {removed_guest}, but due to the new table situation I will need to uninvite you, hope to catch you at the next dinner")

removed_guest = guest_list.pop(1)

print(f"I'm sorry {removed_guest}, but due to the new table situation I will need to uninvite you, hope to catch you at the next dinner")

print(f"Hello {guest_list[0]}, you're still on the list for dinner")
print(f"Hello {guest_list[1]}, you're still on the list for dinner")

del guest_list[0]
del guest_list[0]

print(guest_list)

3-8

dream_locations= ["New Zealand" , "Crete" , "Azores" , "France" , "Costa Rica"]

print(dream_locations)

print(sorted(dream_locations))

print(dream_locations)

print(sorted(dream_locations , reverse=True))

print(dream_locations)

dream_locations.reverse()

print(dream_locations)

dream_locations.reverse()

print(dream_locations)

dream_locations.sort()

print(dream_locations)

dream_locations.sort(reverse=True)

print(dream_locations)

3-9

print(len(guest_list))