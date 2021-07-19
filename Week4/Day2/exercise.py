# # example 1
# my_fav_numbers = set()
# my_fav_numbers.add("1")
# my_fav_numbers.add("2")
# my_fav_numbers.remove("2")

# # example 2
# # no tuples's are immutable

# # example 3
# for x in range(1,21):
#     print(x)

# # example 4
# # float has decimals, ints dont. give everything a decimal value, even if at 0

# #  example 5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# count = 0
# for fruit in basket:
#     if fruit == "Apples":
#         count = count + 1
# print(count)
# basket.clear()
# print(basket)

# # example 6
# my_name = "Gary"
# user_name = input("your name")
# while user_name != my_name:
#     user_name = input("your name")

# # example 7
# for num in you_list:
#     if num % 2 == 0:
#         print(num)

# # example 8
# for num in range(1500,2500):
#     if num % 5 == 0:
#         print(num)
#     elif num % 7 == 0:
#         print(num)   

# # example 9 
# user_fruit = input("your list of fav fruit ")
# list_fruit = user_fruit.split(' ')
# input_fruit = input("select a fruit ")
# no_fruit = True
# for fruit in list_fruit:
#     if input_fruit == fruit:
#         no_fruit = False
#         print("you chose one of your favorite fruits! Enjoy!")
#         break;
# if no_fruit:
#     print("You chose a new fruit. I hope you enjoy")

# # example 10
# sum = 0
# total_toppings =list()
# topping = input("your topping ")
# while topping != 'quit':
#     sum += 1
#     total_toppings += topping
#     print("ill add your toping to the pie")
#     topping = input("your topping ")
# for topping in total_toppings:
#     print(topping)
# sum = (sum * 2.5) + 10   
# print(sum)    

# # example 11
# family = [2,1,3,33,4,19]
# sum = 0
# for age in family:
#     if age < 3:
#         sum += 0
#     elif age < 13:
#         sum += 10 
#     else:
#         sum += 15
# print(sum)    
# age = input("put in your age and done when you are finshed ")
# while age != 'done':
#     age = int(age)

#     if age < 16 and age >12:
#         print(age)
#     if age > 21:
#         print(age)
#     age = input("put in your age and done when you are finshed ")

# # example 12
# names = ["gary","bob", "joe", "bill"]
# good_names = []
# for name in names:
#     age = input("put in your age ")
#     age = int(age)
#     if age > 16:
#         good_names.append(name)
# print(good_names)

# example 13
sandwich_orders = ["tuna","p","steak", "p","p", "egg"]
print("the deli has run out of pastrami ")  
i = 0;
while  i != len(sandwich_orders):
    sandwich_orders.remove("p") 
    i+= 1
finshed_sandwiches = []
for wich in sandwich_orders:
    finshed_sandwiches.append(wich)
for wich in finshed_sandwiches:
    print("i made your " + wich + " sandwich")    