let sent = prompt('Give me a sentence with the word Nemo in it', "your sentence");
sent.toLowerCase()
found = sent.search("nemo")
alert(`"I found Nemo at index ${found}!".`)