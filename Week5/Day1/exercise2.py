# class Circle:
#     def __init__(self,radius= 1):
#         self.radius = radius

#     def find_radius(self):
#         rad = 2 * 3.14 * self.radius
#         return rad    
#     def definition(self):
#         print("this is a circle,2 multiplied by pie by the radius")

# circ1 = Circle()
# print(circ1.find_radius())
# circ2 = Circle(3)
# print(circ2.find_radius())

# # exercise 2

# class MyList:
#     def __init__(self, alist):
#         self.alist = alist

#     def rever(self):
#         print("hi")
#         self.alist.reverse()
#         return self.alist

#     def srt(self):
#         self.alist.sort()
#         return self.alist
# mylist = ["hi","by","goodnight"]
# al = MyList(mylist)
# print(al.rever())
# print(al.srt())

# exercise 3

class  MenuManager:
    def __init__(self):
        menu = {}
        self.menu = menu

    def add_item(self,name, price, spice, gluten):
        lst = [price,spice,gluten] 
        self.menu[name] = lst
        print(self.menu)   

    def update_item(self,name, price, spice, gluten):
        if name in self.menu.keys():
            lst = [price,spice,gluten] 
            self.menu[name] = lst
            print(self.menu) 
        else:
            print("this item doesnt exist in the menu")     

    def remove_item(self,name):
        if name in self.menu.keys():
            del self.menu[name]
            print(self.menu) 
        else:
            print("this item doesnt exist in the menu")     

mnu = MenuManager()
mnu.add_item("pizza","20","cheese",False)
mnu.add_item("Hot Dog","10","MEat",True)
mnu.update_item("Hot Dog","10","Meat",False)
mnu.update_item("Hot-Dog","10","Meat",False)
mnu.remove_item("pizza")
mnu.remove_item("piza")