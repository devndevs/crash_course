class Restaurant:

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

class Flavors:

    def __init__(self , vanilla , chocolate , rocky_road):
        self.vanilla = vanilla
        self.chocolate = chocolate
        self.rocky_road = rocky_road

    def ic_flavors (self):
        print(f"This stand sells the flavors of {self.vanilla}, {self.chocolate} , and {self.rocky_road}. We hope you enjoy our icecream!")

class Icecreamstand(Restaurant):

    def __init__(self , restaurant_name , cuisine_type):
        super().__init__(restaurant_name , cuisine_type)
        self.Flavors = Flavors( "vanilla" , "chocolate" , "rocky road")

stand1 = Icecreamstand( "creamville" , "ice_cream")
stand1.Flavors.ic_flavors()