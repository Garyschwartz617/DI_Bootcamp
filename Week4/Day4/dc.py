matrix = [
    ['7','i','3'],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
]
word = ""
def solve(matr, s):
    i = 0
    while i < 3:
        y = 0
        for x in matr:
            if x[i].isalpha():
                s = s + x[i]
            else:
                s = s + ""  
        i += 1
    return s

print(solve(matrix,word))    
