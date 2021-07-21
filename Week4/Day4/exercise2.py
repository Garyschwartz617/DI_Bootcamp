# # exercise 7
# def get_age(year, month, day):
#     this_year = 2021
#     if month > 7:
#         this_year -= 1
#     elif month == 7 and day >21:
#         this_year -= 1
#     age = this_year - year
#     print(age)
#     return age

# def can_retire(gender, date_of_birth):
#     if gender == "female":
#         if date_of_birth >= 62:
#             print("Yay, you may retire") 
#         else:
#             print("sorry you cant retire")               
#     elif gender == "male":
#         if date_of_birth >= 67:
#             print("Yay, you may retire") 
#         else:
#             print("sorry you cant retire")

# can_retire("female",get_age(1959,7,22))

# exercise 8

def add(x):
    y = x
    y = str(y)
    sum = 0
    sum += x
    x = str(x)
    print(x)
    while len(x) < 4:
        x = x + y
        print(x)
        x = int(x)
        sum += x
        x = str(x)
    return sum    
print(add(3))