person0 = { "first" : "erin" , 
"last" : "darnley" , "age" : 34 , 
"city" : "san diego"}

person1 = { "first" : "ken" , 
"last" : "sikes" , "age" : 33 , 
"city" : "san diego"}

person2 = { "first" : "john" , 
"last" : "tetlow" , "age" : 33 , 
"city" : "manchester"}

people = [ person0 , person1 , person2 ]

for person in people:
    name = person["first"].title() + " " + person["last"].title()
    age= person["age"]
    city = person["city"]
    print(f"{name}, of {city} is {age} years old.")

chadwick = {"name" : "chadwick" , "type" : "dog" , "owner" : "erin"}
bruce = {"name" : "bruce" ,"type" : "cat" , "owner" : "deven"}
luna = {"name" : "luna" ,"type" : "dog" , "owner" : "lauen (Laura + Ken)"}

print()
pets = [ chadwick , bruce , luna]

for pet in pets:
    name = pet["name"].title()
    kind = pet["type"]
    owner = pet["owner"]
    print(f"{name}, is a {kind} and his owner is " +    str(owner).title())

fave_number2 = {"ken" : [42 , 69] , "john" : [ 12 , 603] , "danny" : [15 ,87] ,  "jimmy" : [1 , 90209] , "erin" : [19 , 9] }

for name, number in fave_number2.items():
    print(f"\n{name.title()}'s favorite numners are:")
    for number in number:
        print(f"\t{number}")
    
cities = { "manchester" : { "state" : "new hampshire" , "population" : "113,441" , "fact" : "Adam Sandler is from here"} , 
"chicago" : { "state" : "illinois" , "population" : "8,865,000" , "fact" : "they have the best deep dish"} , "san diego" : { "state" : "california" , "population" : "1,540,000" , "fact" : "some times its called the whales vagina"}}

for city, info in cities.items():
    state = info["state"].title()
    population = info["population"]
    fact = info ["fact"]
    
    print(f"\n" +city.title() + f" is located in the state of {state}")
    print(f"It has a population of about {population}" )
    print(f"Fun Fact: {fact.title()}")