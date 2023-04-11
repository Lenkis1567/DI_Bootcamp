import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit', 'south', 'parallel', 'mother', 'cry', 'computer', 'labirint']
word = random.choice(wordslist) 
print(word)
stars=["*"]*len(word)
print(stars)
tries=0
list_guess=[]
def hang(i:int):
    row1=(''' O''')
    row2=('''/|\ ''')
    row3=('''/ \ ''')
    if i==1:
        print(row1) #1
    if 1<i<=4:
        print(row1)
        print(row2[0:i-1])#2-4
    if 4<i<=6:
        print(row1)#1
        print(row2[0:3])#2-4
        print(row3[0:i-3])#5-6
while tries <6:
    ans=input("Would you like to name a letter(l) or a word(w): ")
    if ans=='w':
        ans_word=input("Input the word: ")
        if ans_word==word:
            print("you won")
            break
        else:
            print("you lost")
            break
    else:
        guess = input('guess a letter: ')
        if guess not in list_guess:
            list_guess.append(guess)
            res = [i for i in range(len(word)) if word.startswith(guess, i)]
            if res==[]:
                tries+=1
                hang(tries)
            else:
                for a in res:
                    stars[a] = guess
                    if "*" not in stars:
                        print("You won")
                        break
            print(stars)
        else:
            print("You've already given this letter, choose another one")


