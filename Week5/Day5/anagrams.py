from anagram_checker import AnagramChecker

while True:
    user_input = input("Either enter a word or exit: ")

    user_input  =user_input.strip().lower()
    if user_input == "exit":
        print("Thank you for your time.")
        break
    elif  " " in user_input:
        print("only one word please")
    elif  user_input.isalpha() == False:
        print("Only letters are allowed in your word")
    else:
        print("good job")
        w = AnagramChecker()
        anagram_list = w.get_anagrams(user_input)
        print(f'''
         YOUR WORD :{user_input}
         This is a valid English word.
         Anagrams for your word: {anagram_list}.

      
        ''')
        break    
# w = AnagramChecker
# w.get_anagrams(user_input)