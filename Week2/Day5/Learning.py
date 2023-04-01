import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'south']
word = random.choice(wordslist) 
print (word)
stars=["*"]*len(word)
print(stars)

for tr in range (0,5):
    guess = input('guess a letter: ')
    for w in enumerate(word):
        if guess == word[w]:
            place = word.index(guess)
            stars[place] = guess
            print(stars)

