class user:

    def __init__(self , first_name , last_name , age , location , interest):
        """initilize user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location
        self.interest = interest

    def describe_user (self):
        """ display summary of the user """
        print(f"\nThis user's name is {self.first_name} {self.last_name} they are {self.age} years old and they live in {self.location}. Their main interest is {self.interest}")

    def greet_user (self):
        """ greet the user"""
        print(f"\nHello {self.first_name} {self.last_name}. Thank you for logging in today, we look forward to helping you learn a new skill!")

user_1 = user("Deven" ,"Perkins" , "31" , "San Diego" , "Sailing")
user_1.describe_user()
user_1.greet_user()

user_2 = user("Ken" , "Sikes" , "2423423" , "Satan's Anus" , "chugging butholes")
user_2.describe_user()
user_2.greet_user()

user_3 = user("John" , "Tetlow" , "23" , "his mom's basement" , "staying in college")
user_3.describe_user()
user_3.greet_user()