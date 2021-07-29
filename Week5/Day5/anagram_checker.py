class AnagramChecker:
    def __init__(self) -> None:
        # with open("sowpods.txt",mode='r',encoding = 'utf-8') as f:
        #     secret_data = f.read() # /f.readlines() 
        # self.secret_data = secret_data
        with open("sowpods.txt",mode='r',encoding = 'utf-8') as f:
            secret_datas = f.readlines() # /f.readlines() 
        lst = []
        for word in secret_datas:
            lst.append(word.replace("\n", "").lower())
        self.secret_list = lst

    def is_valid_word(self,word):
        if word in self.secret_list:
            return True
        else:
            return False        

    def get_anagrams(self,word):
        final_word_list = []
        for arg in self.secret_list:
            if self.is_anagram(word,arg):
                final_word_list.append(arg)
        return final_word_list            

    def is_anagram(self,word1, word2):
        list1 = []
        list2 = []
        for letter1 in word1:
            list1.append(letter1)
        for letter2 in word2:
            list2.append(letter2)
    
        for letter1 in list1:
                if letter1 in list2:
                    list2.remove(letter1)
                else:
                    return False    
        if list2 == []:
            return True
        else:
            return False   





# w = AnagramChecker()
# print(w.is_valid_word("AA"))
# print(w.is_anagram("lower","team")) 
# print(w.get_anagrams("team"))          