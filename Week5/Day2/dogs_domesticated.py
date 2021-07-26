from exercise1 import Dog
import random
class Petdog(Dog):
    trained = False
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
        

    def train(self):
        self.bark()
        self.trained = True 

    def play(self,*args):
        lst = ""
        for ar in args:
            lst = lst +" " + ar.name
        print(f"{lst} all play together")  

    def do_a_trick(self):
        if self.trained:
            x = random.randint(0,3) 
            if x == 0:
                print(f"{self.name} does a barrel roll")       
            elif x == 1:
                print(f"{self.name} stands on his back legs")
            elif x == 2:
                print(f"{self.name} shakes your hand") 
            elif x == 3:
                print(f"{self.name} plays dead")

dg1 =Petdog("joe",3,50)            
dg2 =Petdog("moe",3,50)            
dg3 =Petdog("seven",3,50)            
dg4 =Petdog("star",3,50)
dg1.train()
dg3.train()
dg4.train()

dg1.do_a_trick()
dg2.do_a_trick()
dg3.do_a_trick()
dg4.do_a_trick()
dg1.play(dg1,dg2,dg3,dg4)