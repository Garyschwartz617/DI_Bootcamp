import random
# # question 1
# def display_message():
#     print ("I am learning functions in Python")
# display_message()   

# # question 2
# def favorite_book(title):
#     print(f"one of my favorite boooks is {title}")

# favorite_book("alice in wonderland")

# # question 3
# def describe_city(city,country= "USA"):
#     print(f"{city} is in {country}")
# describe_city("Jerusalem", "Israel")    

# # question 4
# rand = random.randint(1,101)
# user_number = input("your number")
# def compare(rand,user_number):
#     i = int(user_number)
#     if rand == i:
#         print("success")
#     else:
#         print(f"FAIL: your number was {user_number} the random number was {rand}")  
# compare(rand,user_number)        

# # question 5
# def make_shirt(txt= "I love Python", size="large"):
#     print(f"The size of the shirt is {size} and it says {txt}")
# make_shirt("hi","large")
# make_shirt()  

# question 5
magicians =["hudiny","Bennett", "Gambit"]
def show_magicians(magicians):
    for magician in magicians:
        print( make_great(magician))

def make_great(mag):
    return mag + " The Great"
show_magicians(magicians)
