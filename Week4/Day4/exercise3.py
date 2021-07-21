import random

# def get_random_temp(season):
#     if season == "summer":
#         temp = random.randint(30,40)
#         return temp
#     if season == "winter":
#         temp = random.randint(-10,10)
#         return temp
#     if season == "spring":
#         temp = random.randint(0,30)
#         return temp
#     if season == "fall":
#         temp = random.randint(0,30)
#         return temp

# def main():
#     season = input("what season are we in? ")
#     temp = get_random_temp(season)
#     print(f"The temperature right now is {temp} degrees Celsius. in {season}")
#     if temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif temp <16:
#         print("Quite chilly! Don’t forget your coat")  
#     elif temp <23:
#         print("perfect day for a sweat shirt") 
#     elif temp < 32:
#         print("perfect day!!!!") 
#     else:
#         print("TOOO hot, stay inside")    
# main()    

def throw_die():
    die = random.randint(1,6)
    return die
# print(throw_die())

# die1 = throw_die()
# die2 = throw_die()
def throw_until_doubles():
    die1 = throw_die()
    die2 = throw_die()
    print(die1,die2)
    x = 1
    while die1 != die2:
        die1 = throw_die()
        die2 = throw_die()
        print(die1,die2)
        x +=1
    return x    

# print(throw_until_doubles())

def main():
    x = 0
    y = 0
    while x < 100:
        z = throw_until_doubles()
        y = y + z
        x+=1
    print(f"The toal throws was: {y}")  
    print(f"the average throw was: {y/100}")  
main()   