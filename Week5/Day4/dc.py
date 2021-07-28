import string
from nltk.corpus import stopwords
class Text:
    with open("book.txt",mode='r',encoding = 'utf-8') as f:
        secret_data = f.read() # /f.readlines() 

    def __init__(self,txt=secret_data):
        self.txt = txt

    @classmethod
    def txt_file(cls):
        return cls.secret_data
    
    def feq(self,wrd):
        wrd = " " + wrd + " "
        i = self.txt.count(wrd)
        return i

    def each_word(self):
        lst = []
        x = self.txt.replace(".","").replace("!","").replace(",","").replace("?","").lower()
        lst_txt = x.split()
        for word in lst_txt:
            if word not in lst:
                lst.append(word)
        return lst        

    def most(self):
        lst = []
        x = self.txt.replace(".","").replace("!","").replace(",","").replace("?","").lower()
        lst_txt = x.split()
        for word in lst_txt:
            if word not in lst:
                lst.append(word)
        highest_word = ""
        highest = 0
        for ls in lst:
            this_count = 0
            for word in lst_txt:
                if ls == word:
                    this_count+=1
            if this_count > highest:
                highest = this_count
                highest_word = ls 
        print(highest)               
        return highest_word

class TextModification(Text):
    def no_punctuation(self):
        x = self.txt.replace(".","").replace("!","").replace(",","").replace("?","")
        return x

    def stop_word(self):
        lst = []
        bd = stopwords.words('english')
        lst_txt = self.txt.split
        for word in lst_txt:
            if word not in bd:
                lst.append(word)
        x = " ".join(lst)
        return x    

    def no_charct(self):
        st = ""
        for ltr in self.txt:
            if ltr.isalnum():
                st += ltr
        return st

with open("book.txt",mode='r',encoding = 'utf-8') as f:
    secret_data = f.read() # /f.readlines() 
t = Text()
print(t.txt_file())
# print(t.feq("I"))
y = TextModification(secret_data)
# print(y.no_charct())
# print(y.no_punctuation())
# print(y.stop_word())
# print(t.each_word())
# print(t.most())