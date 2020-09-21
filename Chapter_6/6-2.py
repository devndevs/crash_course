fave_number2 = {"ken" : 42 , "john" : 12 , "danny" : 15 ,  "jimmy" : 1 , "erin" : 19 }
for name, number in fave_number2.items():
    print(f"\n{name.title()}'s favorite number is {number}.")

glossary = { "loop" : "a loop is used to print multiple lines of code" , 
"syntax" : "syntax is important because it is how the code will print" , 
"print" : "print will print your programs commands" , 
"if" : "an if will check a progream for conditions" , 
"elif" : "elif is added after an if statement to check for other conditions" , 
"dictionary" : "what this list is stored in" , 
"key" : "the name of someting in a dictionary" , 
"value" : "the stored information from the key in the dictionary" , 
"set" : "a set will help eliminate redundancies" , 
"else" : "if none of the other conditions are met, else will produce the programmed responce"}

for name, know in glossary.items():
    print(f"\n{name.title()}: {know}.")

rivers = {"nile" : "africa" , "colorado" : "untied states of america" , "tames" : 'england'}
for river, through in rivers.items():
    print(f"\nThe {river.title()}, runs through {through.title()}")


rivers = {"nile" : "africa" , "colorado" : "untied states of america" , "tames" : 'england'}
for river, through in rivers.items():
    print(f"\n{river.title()}")

rivers = {"nile" : "africa" , "colorado" : "untied states of america" , "tames" : 'england'}
for river, through in rivers.items():
    print(f"\n{through.title()}")

favorite_languages = { "jen" : "python" , "sarah" : "c" , "edward" : "ruby" , "phil" : "python" , "ken" : "python" , "john" : "java"}
friends = [ "erin" , "danny" , "rob" , "tom" , "ken" , "john"]
for name in favorite_languages:
    print(f"\n{name.title()}, thank you for taking the poll")
for friends in friends:
    if friends not in favorite_languages.keys():
        print(f"\n{friends.title()}, please take the poll.")
