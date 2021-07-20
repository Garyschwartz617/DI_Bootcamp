# # example 1
# import random
# x = 0
# l =[]
# while x < random.randint(1,500):
#     l.append(random.randint(-100,101))
#     x += 1
# print(l)  

# example 2
users = {
    "gary": "hello123",
    "adina": "yoyoyo789",
    "joe": "highfive2"
}
signed_in = []
x = 0
not_taken = True
while x == 0:
    user_input = input('either exit or login or signup: ')
    if user_input =="exit":
        break
    if user_input == "login":
        user_name = input("input your username: ")
        for name in users:
            if user_name == name:
                signed_in.append(user_name)
                print("you are logged in")
        break
    if user_input =="signup":
        while x == 0:
            new_user_name = input("input your new username: ")
            for name in users:
                if new_user_name == name:
                    print("username unavaliable, try again.")
                    not_taken = False
                    break
                else:
                    not_taken = True    
                # break    
            if not_taken:    # else:
                new_password = input("your new password: ")
                users[new_user_name] = new_password 
                break
            
        # break
print(users)


# if user_input == "login":
#     user_name = input(" input your username: ")           