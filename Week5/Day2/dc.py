import random
class Gene():
    def __init__(self):
        self.x = random.randint(0,1)
        
    def code(self):
        return self.x

    def  mutate_gene(self):
        if self.x == 0:
            self.x = 1
        else:
            self.x = 0



class Chromosome(Gene):
    def __init__(self):
        self.chro = [Gene() for x in range(3)]

    def  mutate_chro(self):
        for chr in self.chro:
            y = random.randint(1,100)
            if y > 50 :
                chr.mutate_gene()

    def print_chro(self):
        lst = []
        for chr in self.chro:
            lst.append(chr.code())
        # print(lst)
        return lst    



class DNA(Chromosome):        
    def __init__(self):
        self.dna = [Chromosome() for x in range(3)]

    def print_gene(self):
        fst = []
        for gn in self.dna:
            # gn.print_chro()
            fst.append(gn.print_chro())
        print(fst)
        return fst
        # return gn.print_chro()


    def mutate_gene(self):
        lst = []
        for gne in self.dna:
            # gne.mutate_chro()
            lst.append(gne.mutate_chro())
        return lst    

class Organism(DNA):
    def __init__(self,environment):
        super().__init__()
        self.environment = environment

    def  mutate_chro(self):
        for chr in self.dna:
            y = random.randint(1,100)
            if y > self.environment:
                chr.mutate_gene()


q = DNA()
w =Organism(99)
# w.print_gene()
# w.mutate_gene()
# print("hello")
# w.print_gene()
# w.mutate_gene()
# print("hello")
# w.print_gene()
x = True
lst = []
y = 1
for n in w.print_gene():
    for f in n:
        lst.append(f)
                
print(lst)            
while x:
    lst = []
    for n in w.print_gene():
        for f in n:
            lst.append(f)

    print(y)
    y+=1
    if 0 in lst:
        w.mutate_gene()
    else:
        x = False 
