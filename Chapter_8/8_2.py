def make_shirt(text,size):
    print(f"Thank you for ordering a shirt from us in the size {size} and with the message printed on it that reads: ''{text}.'' ")

make_shirt("I think it's turning into fall" , "medium")

def make_shirt_2(text = "I think it's turning into fall",size= "Medium"):
    print(f"\nThank you for ordering a shirt from us in the size {size} and with the message printed on it that reads: ''{text}.'' ")

make_shirt_2()

def large_shirts(text = "I love Python", size = "large"):
    print(f"\nThank you for ordering a shirt from us in the size {size} and with the message printed on it that reads: ''{text}.'' ")

large_shirts()
large_shirts(size = "medium")
large_shirts(text = "it think it's turning into winter")

def describe_city(city , country = "New Zealand"):
    print(f"\n{city} is in {country}")

describe_city("Aukland")
describe_city("Christchurch")
describe_city("Queenstown")
describe_city("London" , country = "The United Kingdom")