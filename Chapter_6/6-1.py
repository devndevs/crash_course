person = { "first_name" : "erin" , "last_name" : "darnley" , "age" : 34 , "city" : "san diego"}
print(person[f"first_name"].title() , person[f"last_name"].title())
print (f"is" , person["age"] , "and she lives in the city of" , person["city"].title())

fave_number = { "friend1" : "ken" , "ken" : 69 , "friend2" : "john" , "john" : 12 , "friend3" : "danny" , "danny" : 15 , "friend4" : "jimmy" , "jimmy" : 1 , "friend5" : "erin" , "erin" : 19 }
print(f"\n" , fave_number["friend1"].title() + "'s favorite number is" , fave_number["ken"])
print(f"\n" , fave_number["friend2"].title() + "'s favorite number is" , fave_number["john"])
print(f"\n" , fave_number["friend3"].title() + "'s favorite number is" , fave_number["danny"])
print(f"\n" , fave_number["friend4"].title() + "'s favorite number is" , fave_number["jimmy"])
print(f"\n" , fave_number["friend5"].title() + "'s favorite number is" , fave_number["erin"])

glossary = { "loop" : "a loop is used to print multiple lines of code" , "syntax" : "syntax is important because it is how the code will print" , "print" : "print will print your programs commands" , "if" : "and if will check a progream for conditions" , "elif" : "elif is added after an if statement to check for other conditions"}
print(f"\n Loop: " + glossary["loop"])
print(f"\n Syntax: " + glossary["syntax"])
print(f"\n if: " + glossary["if"])
print(f"\n elif: " + glossary["elif"])
print(f"\n print: " + glossary["print"])