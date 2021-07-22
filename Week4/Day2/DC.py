bday = input("bday on DD/MM/Year ")
print(bday)
lst = bday.split("/")
year = lst[2]
year = int(year)
age = 2021 - year
print(age)
age = str(age)
dig = list(age)
print(dig)
num = dig[len(dig)- 1]
print (num)
num = int(num)
if (11 - num)%2 == 0:
    i = ""
    n = ""
    p = 0
    while p != num:
        i += "i"
        p+=1
    print(i)   
    top = (11 - num)/2
    z = 0
    while z != top:
        n += "_"
        z += 1    
    print("    " + n + i + n  + "    ")
else:
    i = ""
    n = ""
    top = (10 - num)/2  
    z = 0
    while z != top:
        n += "_"
        z += 1    
 
    num = num/2
    p = 0
    while p != num:
        i += "i"
        p+=1
    print("    " + n + i +"_"+ i + n  + "    ")
print("   |:H:a:p:p:y:|   ")
print(" __|___________|__ ")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")