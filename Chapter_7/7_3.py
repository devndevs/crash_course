prompt = ("\n Please enter the age of who the movie ticket will be for ")
prompt += ("\n When finished please type 'done' , thank you ")

while True:
    age = input(prompt)
    if age == "done":
        break
    age = int(age)
    
    if age < 3:
        print (f"\nYour child can get in for free")
    elif age >= 3 and age <= 12:
        print(f"\nIt will cost $12 for your child's ticket")
    elif age > 12:
        print (f"\n The cost of this ticket is $15")
    
