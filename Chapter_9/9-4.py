class user:

    def __init__(self , first_name , last_name , age , location , interest):
        """initilize user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location
        self.interest = interest
        self.login_attempts = 0

    def increment_login_attempts (self):
        self.login_attempts += 1

    def reset_login_attempts (self):
        if self.login_attempts <= 1:
            self.login_attempts
        else:
            self.login_attempts = 0

    def describe_user (self):
        """ display summary of the user """
        print(f"\nThis user's name is {self.first_name} {self.last_name} they are {self.age} years old and they live in {self.location}. Their main interest is {self.interest}")

    def greet_user (self):
        """ greet the user"""
        print(f"\nHello {self.first_name} {self.last_name}. Thank you for logging in today, we look forward to helping you learn a new skill!")

user1 = user("Deven" , "Perkins", "32" , "San Diego" , "sailing")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print (user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print (user1.login_attempts)
user1.reset_login_attempts()
print (user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print (user1.login_attempts)
user1.reset_login_attempts()
print (user1.login_attempts)




