# # exercise1
# import random

# def get_words_from_file():
#     with open("sowpods.txt",mode='r',encoding = 'utf-8') as f:
#         secret_data = f.readlines() # /f.readlines() 
#     return secret_data 
# # print(get_words_from_file())
# def get_random_sentence(leng):
#         i = 0
#         lst =[]
#         while i < leng:
#             rnd_wrd = random.choice(get_words_from_file())
#             lst.append(rnd_wrd)
#             i+=1
#         sent = "".join(lst).replace("\n", " ").lower()
#         return sent

# # print(get_random_sentence(5)) 

# def main():
#     print("you put in a number, and we will return you a sentence with that many words")
#     nm = input("your number greater then 2 and less then 20: ")
#     nm = int(nm)
#     if nm > 2 and nm < 20:
#          print(get_random_sentence(nm))
#     else:
#         print("wrong data")
# main() 

# exercise 2 

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
js =json.loads(sampleJson)
print(js["company"]["employee"]["payable"]["salary"])
js["company"]["employee"]["birth_date"] = "8/22/1997"
print(js)
with open('exercise.json', 'w') as f:
    json.dump(sampleJson, f,indent="2")
