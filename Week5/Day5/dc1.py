import time
import requests
lst = ["http://google.com","https://www.imdb.com","https://www.ynet.co.il/home/0,7340,L-8,00.html"]
for l in lst:
    before = time.time()
    response = requests.get(l)
    if response.status_code == 200:
            after = time.time()   
    else:
        print('unknown error, code:', response.status_code)

    after = time.time()
    print(after-before)

