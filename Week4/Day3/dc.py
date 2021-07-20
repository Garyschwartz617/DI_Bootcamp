text = input('your english: ')
cypher_text = ""
for letter in text:
    cypher_text += chr(ord(letter) + 3)
print(cypher_text) 
gibberish = input("your gibberish: ")
decipher = ""
for letter in cypher_text:
    decipher += chr(ord(letter) - 3)
print(decipher)    