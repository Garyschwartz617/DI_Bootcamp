# # exercise1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat_one = Cat("tibby",8)  
# cat_two = Cat("Mabel",10) 

# def oldest_cat(one,two):
#     if one.age > two.age:
#         print(f"The oldest cat is {one.name}, and is {one.age} years old.")
#     elif one.age < two.age:
#         print(f"The oldest cat is {two.name}, and is {two.age} years old.")
#     else:
#         print("they are both the same age")    
# oldest_cat(cat_one,cat_two)

# # exercise2

# class Dog:
#     def __init__(self,name,height):
#         self.name = name
#         self.height = height
        
#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high") 

# davids_dog = Dog("rex", 50)
# print(davids_dog.name )
# print(davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name )
# print(sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()
# if sarahs_dog.height > davids_dog.height:
#     print(f"{sarahs_dog.name} is bigger")
# else:
#      print(f"{davids_dog.name} is bigger")   

# # example 3

# class Song:
#     def __init__(self,lyrics):
#         self.lyrics = list(lyrics)

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)    

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

# example 4

class Zoo:
    def  __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal in self.animals:
            print("this animal is already in the zoo")
            print(self.animals)
        else:
            self.animals.append(new_animal)
            print(self.animals) 

    def get_animals(self):
        print(self.animals) 

    def sell_animals(self,animal_sold):
        if animal_sold in self.animals:
            print(f"this {animal_sold} has been sold")
            self.animals.remove(animal_sold)
            print(self.animals)
        else:
            print("cnt sell an animal you dont have")
            print(self.animals) 
             
    def sort_animals(self):
        self.animals.sort()
        dic = {}
        for anim in self.animals:
            dic[f"{anim[0]}"] = anim
        for keys in dic.keys():
            ls = []
            for anim in self.animals:
                if keys == anim[0]:
                    ls.append(anim)
            dic[keys] = ls
        # for amount in dic:
        
        #     print (f"{amount.values()} :")
        print(dic.values())


zoo1 = Zoo("Ramat-Gan-Zoo") 
zoo1.add_animal("zebra")
zoo1.add_animal("monkey")
zoo1.add_animal("ape")
zoo1.add_animal("baboon")
zoo1.add_animal("bear")
zoo1.add_animal("emu")
zoo1.add_animal("cat")
zoo1.add_animal("couger")
zoo1.add_animal("eel")
zoo1.add_animal("zebra") 
zoo1.sell_animals("zebra") 
zoo1.add_animal("Cat") 
zoo1.sort_animals()                                                              