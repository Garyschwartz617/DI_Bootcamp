# example 1
# print(abs(-10))
# print(input("your name: "))
# print(int(2.34))

# class A():

#     def __doc__():
#         return ' this is what i do'
# print(A.__doc__())  

# example 2 
# print(dir(int))
class Currency():
    def __init__(self,country_bill, amount):
        self.country_bill = country_bill
        self.amount = amount
        
    
    def __str__(self):
        return f'{self.amount} {self.country_bill}'

    def __int__(self): 
        return int(self.amount)
   
    def __repr__(self):
        return f'{self.amount} {self.country_bill}'

    def __add__(self,other):
        if isinstance(other,int):
            return self.amount + other
        elif isinstance(other,Currency):
            return self.amount + other.amount

    def __iadd__(self,other):
        # def __iadd__(self, other):
        # return self.amount + other.amount if self.country_bill == other.country_bill else ValueError
        if isinstance(other,int):
            self.amount = self.amount + other
            return f'{self.amount} {self.country_bill}'
        else:
            return str(self.amount + other.amount) + self.country_bill if self.country_bill == other.country_bill else TypeError(f"Cannot add between Currency type {self.country_bill} and {other.country_bill}")
    
        # elif isinstance(other,Currency) and self.country_bill == other.country_bill:
        #     self.amount = self.amount + other.amount        
        #     return self.amount
        # elif isinstance(other,Currency) and self.country_bill != other.country_bill:
        #     raise TypeError(f"Cannot add between Currency type {self.country_bill}and {other.country_bill}")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# print(str(c1))
# print(int(c1))
# print(repr(c1)) 
# print(c1 +5)
# print(c1 + c2)
print(c1)
c1 += c4
print(c1)
c1 += c2
print(c1)
c1 + c3                         