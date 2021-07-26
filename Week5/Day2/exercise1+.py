class Family():
    def __init__(self,lastname,*family,):
        # self.family = family
        self.lastname = lastname
        self.lst = []
        self.family = family
        for fm in self.family:
            self.lst.append(fm)
        # for sf in self.lst:
        #     print(sf)
        # print(self.lst)
   
    def born(self,name,age,gender,is_child):
        dict = {}
        dict["name"] = name
        dict["age"] = age
        dict["gender"] = gender
        dict["is_child"] = is_child
        self.lst.append(dict)

    def members(self):
        for sf in self.lst:
          print(sf)
 
    def is_18(self, name):
        for sf in self.lst:
            if sf["name"] == name and sf["age"] >= 18:
                print(True)
            elif sf["name"] == name:
                print(False)    


class Person():
    def __init__(self,name,age,gender,is_child):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_child = is_child
        self.info = {}
        self.info["name"] = name
        self.info["age"] = age
        self.info["gender"] = gender
        self.info["is_child"] = is_child
        
    def dct(self):
        return self.info

   

# pr1 = Person("Gary",27,"Male", False)
# pr2 = Person("Adina",23,"Female", False)
# pr3 = Person("Joe",3,"Male", False)

# fm = Family("schwartz",pr1.dct(),pr2.dct(),pr3.dct())
# fm.born("hello",2,"Female",True)
# fm.members()
# fm.is_18("Gary") 
# fm.is_18("hello")


# example 2

class Incredible(Person):
    def __init__(self, name, age, gender, is_child,power,incredible_name):
        super().__init__(name, age, gender, is_child)
        self.info["power"] = power
        self.info["incredible_name"] = incredible_name
       

class TheIncredibles(Family):
    def use_power(self,name):
        for sf in self.lst:
            if sf["name"] == name and sf["age"] >= 18: 
                pwr = sf["power"]
                print(pwr)
            elif sf["name"] == name:
                print(False)    
    def incredible_presentation(self):
        for sf in self.lst:
          print(sf["name"],sf["incredible_name"],sf["power"])

    def born(self,name,age,gender,is_child,power,incredible_name):
        # super().born(name,age,gender,is_child)
        dict = {}
        dict["name"] = name
        dict["age"] = age
        dict["gender"] = gender
        dict["is_child"] = is_child
        dict["power"] = power
        dict["incredible_name"] = incredible_name
        self.lst.append(dict)

pr1 = Incredible("Bob",45,"Male",False,"Super Strength","Mr. Incredible")
pr2 = Incredible("Helen",43,"Female",False,"Elastic Limbs","Elastagirl")
pr3 = Incredible("Violet",15,"Female",True,"Invisable/Forcefield","InvisOgirl")
pr4 = Incredible("Dash",11,"Male",True,"Super Speed","-")

incr = TheIncredibles("Parr",pr1.dct(),pr2.dct(),pr3.dct(),pr4.dct())
incr.incredible_presentation()
incr.use_power("Helen")
incr.use_power("Dash")
incr.members()
incr.born("Jack-Jack",2,"Male",True,"Unknown","We Will find out")
incr.incredible_presentation()