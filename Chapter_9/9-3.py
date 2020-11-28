class restaurant:

    def __init__(self , restaurant_name , cuisine_type):
        """initilizs restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant (self):
        """ Display a summary of the restaurant"""
        print(f"\nWelcome to {self.restaurant_name}, we're glad you came. the type of food we serve here is {self.cuisine_type}")

    def open_restaurant(self):
        """ Show if the restaurant is open"""
        print(f"\n{self.restaurant_name} is now open, come on in!")

    def set_number_served(self , people):
        self.number_served = people

    def increment_number_served (self, people):
        self.number_served += people

    def get_number_served (self):
        print(f"\n{self.number_served} have been served here")

served = restaurant( "Siako" , "sushi")
served.set_number_served(8)
served.open_restaurant()
served.get_number_served()
served.set_number_served(15)
served.get_number_served()
served.increment_number_served(10)
served.get_number_served()
served.increment_number_served(10)
served.get_number_served()
served.increment_number_served(10)
served.get_number_served()
served.increment_number_served(10)
served.get_number_served()
served.increment_number_served(10)
served.get_number_served()




