import datetime
# # exercise1
# def time():
#     today_date = datetime.date.today()
#     # actual_datetime = datetime.datetime.now()
#     return today_date
# print(time()) 

# # exercise 2
# def until_Jan():
#     x = datetime.date(2022,1,1)
#     z = datetime.date.today()
#     y = x - z
#     return y

# print(until_Jan()) 

# # exercise 3
# def been_alive(year,month,day):
#     x = datetime.date(year,month,day)
#     z = datetime.date.today()
#     y = z -x
#     return y
# print(been_alive(1994,6,17)) 

# # example 4
# def  until_holiday():
#     today_date = datetime.datetime.now()
#     print(today_date)
#     x = datetime.datetime(2021,8,27,0,0,0)
#     y = x - today_date
#     print(y)
# until_holiday()    

# def planet():
#     today_date = datetime.datetime.now()
#     birthdate = datetime.datetime(1994,6,17,7,15,38)
#     y = today_date -birthdate
#     sec = y.total_seconds()
#     print(sec) 
#     mercsecs = sec/0.2408467
#     merc = mercsecs/60/60/24/365
#     print(f'I am {merc} mercurys year old')
#     vensecs = sec/0.61519726
#     venus = vensecs/60/60/24/365
#     print(f'I am {venus} venus year old')
#     marsecs = sec/1.8808158
#     mar = marsecs/60/60/24/365
#     print(f'I am {mar} mars year old')
#     jupsecs = sec/11.862615
#     jup = jupsecs/60/60/24/365
#     print(f'I am {jup} jupiter year old')
#     satsecs = sec/29.447498
#     sat = satsecs/60/60/24/365
#     print(f'I am {sat} saturn year old')
#     urasecs = sec/84.016846
#     ura = urasecs/60/60/24/365
#     print(f'I am {ura} uranus year old')
#     neptsecs = sec/164.79132
#     nept = neptsecs/60/60/24/365
#     print(f'I am {nept} neptune year old')

# planet()

# example 6
from faker import Faker

fake = Faker()
print(fake.name())
user = []
def fillup(name,address,langage_code):
    person ={}
    person["name"] = name
    person["adress"] = address
    person["langage_code"] = langage_code
    user.append(person)
 

fillup(fake.name(),fake.address(),fake.language_code())
print(user)