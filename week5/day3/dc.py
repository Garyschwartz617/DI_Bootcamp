class Circle():
    lst = []
    def __init__(self,radius = None,diamter = None):
        self.radius = radius
        self.diamter = diamter
        self.lst.append(self)
        print(self)

    def get_radius(self):
        print(self.radius)   

    def get_diamter(self):
        print(self.diamter+0)

    def area(self):
        if self.diamter == None:
            area =  3.14 *self.radius* self.radius
            print(area) 
        else:
            rad = self.diamter/2
            area = 3.14 * rad * rad
            print(area) 

    @classmethod
    def sort(cls):
        cls.lst.sort()   
        return cls.lst

    @staticmethod
    def are_round():
        print('circles are round like pizza' )

    def __add__(self,other):
        if isinstance(other,Circle):
            return self.radius + other.radius

    def __lt__(self,other):
        if self.radius < other.radius:
             return True
        else:
              return False         

    def __gt__(self,other):
        if self.radius > other.radius:
             return True
        else:
              return False         

    def __eq__(self,other):
        if self.radius == other.radius:
             return True
        else:
              return False         

a = Circle(4,6)
b = Circle(3,8)
a.get_radius()
a.get_diamter()
a.area()
a.are_round()
print(a + b)
print(b < a)
print(a > b)
print(a == b)
print(a.sort())
