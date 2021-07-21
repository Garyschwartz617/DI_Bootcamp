# s = input("String: ")
# ch = input("Character: ")

# def rep(s,ch):
#     x = 0
#     for c in s:
#         if c == ch:
#             x +=1

#     return x
# print(rep(s,ch))    


def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index
     print(f"hi  {alist}")
    #  print(index)
     print(currentvalue)
     print(alist[position-1])
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
         print(alist)

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)