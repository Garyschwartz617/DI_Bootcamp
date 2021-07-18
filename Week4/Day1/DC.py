import random
cdd = input("just 10 characters")
if(len(cdd) < 10):
    print("string not long enough")
elif(len(cdd) > 10):
    print("string too long")
else:
    print( "first character is "+cdd[0]+ ".Last character is " + cdd[9])    

y = ""
for x in cdd:
    y = y + x
    print(y)

thislist = []   
for x in cdd:
    thislist.append(x)
yes = random.shuffle(thislist) 
t = ''.join(thislist)    
print(t)