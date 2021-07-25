class Farm:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}'s farm")
        self.dct = {}

    def add_animal(self, animal_name, amount= 1):
        if animal_name in self.dct.keys():
            self.dct[f"{animal_name}"] = self.dct[f"{animal_name}"] + amount
        else:
            self.dct[f"{animal_name}"] = amount   
    def get_info(self):
        for index, amount in enumerate(self.dct):
            print (f"{amount} : {index}")
        print("E-I-E-I-O")  


mc = Farm("OL McDonalds")          
mc.add_animal("cow", 5)
mc.add_animal("sheep" )
mc.add_animal("sheep" )
mc.add_animal("goat", 12)
mc.get_info()