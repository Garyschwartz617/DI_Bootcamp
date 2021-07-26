# # example1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Striped(Cat):
#     def run(self):
#         print("im running")

# cat1 = Cat("hi",1)
# cat2 = Cat("bye",3)
# cat3 = Cat("yes",4)
# cat4 = Cat("hello",5)
# my_cats = [cat1,cat2,cat3,cat4]
# my_pets = Pets(my_cats)
# my_pets.walk()

# example2
class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return(f"{self.name} is barking")

    def run_speed(self):
        return self.weight/self.age/3

    def fight(self,other_dog):
        if other_dog.run_speed() > self.run_speed():
            print(f"{other_dog.name} won the fight")
        elif other_dog.run_speed() < self.run_speed():
            print(f"{self.name} won the fight!")
        else:
            print("it was a tie")  

# dog1 = Dog("joe",3,30) 
# dog2 = Dog("Moe",5,100) 
# dog3 = Dog("joe",3,30)            

# print(dog2.bark())
# dog1.fight(dog2)
# dog1.fight(dog3)
# dog2.fight(dog1)