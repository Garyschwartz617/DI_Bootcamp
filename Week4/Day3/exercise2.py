# example 1-3
# birthdays = {
#     "adina": "1995/12/04",
#     "gary": "1994/06/17",
#     "joe": "2000/12/23"
# }
# new_name = input("put in someones name: ")
# new_birthday = input("put in that someones birthday YYYY/MM/DD: ")
# birthdays[new_name] = new_birthday
# print("You can look up the birthdays of the people in the list!")
# print(list(birthdays.keys()))
# user_name = input("your name, please: ")
# for name in birthdays:
#     if name == user_name:
#         print("hi your birthday is "+ birthdays[name])
#         break
# else:
#     print("you birthday is not here " + user_name)

# # example 4
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }   
# sent = "here are your items with there prices " 
# for item in items:
#     v = str(items[item])
#     sent += item + " " + v + " "
# print(sent)   
# for item in items:
#     l = []
#     v = items[item]
#     stock = 5
#     l.append(v)
#     l.append(stock)
#     items[item] = l   
# print(items)  
# sum = 0
# for item in items:
#     thing = items[item][0] * items[item][1]
#     sum += thing
# print(sum)    

# example 5
cars = "Volkswagen, by, Toyota, Ford Motor, Honda, Chevrolet, hi"
carslist = cars.split(", ")
print(carslist)
print(len(carslist))
carslist.sort(reverse = True)
print(carslist)
new_list = [c for c in carslist if  c.find("o") != -1]
print(new_list)
new_list2 = [c for c in carslist if  c.find("i") == -1]
print(new_list2)