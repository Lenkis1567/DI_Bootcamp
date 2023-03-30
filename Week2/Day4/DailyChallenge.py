matrix = ["7i3", "Tsi", "h|x", "i #", "sM ", "$a ", "#t%", "^r!"]
alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "?", "!"]

for word in matrix:
    for letter in word:
        print(f"{letter}", end="")
    print("")
sentence1 = []
sentence_result = []
i = len(matrix)
y = len(matrix[0])
nonalfa = 0
for y1 in range(0,y):
    for i1 in range(0,i):
        sentence1.append(matrix[i1][y1])
    # print(sentence1)
for z in sentence1:
    if z.casefold() in alfa:
        sentence_result.append(z)
        nonalfa = 0
    else:
        nonalfa +=1
        if nonalfa == 2:
            sentence_result.append(" ")
    

print("".join(sentence_result))   


