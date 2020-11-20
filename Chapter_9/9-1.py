class restaurant:

    def __init__(self , restaurant_name , cuisine_type):
        """initilizs restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant (self):
        """ Display a summary of the restaurant"""
        print(f"\nWelcome to {self.restaurant_name}, we're glad you came. the type of food we serve here is {self.cuisine_type}")

    def open_restaurant(self):
        """ Show if the restaurant is open"""
        print(f"\n{self.restaurant_name} is now open, come on in!")

r1 = restaurant("rice" , "Sushi")
r1.describe_restaurant()
r1.open_restaurant()

r2 = restaurant ("the friendly" , "pizza")
r2.describe_restaurant()
r2.open_restaurant()

r3 = restaurant ("shank and bone" , "pho")
r3.describe_restaurant()
r3.open_restaurant()

r4 = restaurant( "tajima" , "ramen")
r4.describe_restaurant()
r4.open_restaurant()
