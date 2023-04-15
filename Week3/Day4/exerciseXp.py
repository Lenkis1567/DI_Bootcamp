import random
with open('words.txt', 'r') as words:
    def get_words_from_file():
        words_list=words.readlines()
        length=len(words_list)
        return words_list
    def get_random_sentence(words_list, length): #(как это сделать без параметра words_list??)
        random_words=[]
        for n in range(0,length):
            number_word=random.randint(0, len(words_list))
            random_word=words_list[number_word]
            random_word_st= random_word.strip('\n')
            random_word_st1=random_word_st.lower()
            random_words.append(random_word_st1)
        return random_words
    def main():
        print("This is a program to give you a list of random words")
        length=int(input("How many words the sentence should have, input a unber from 2 to 20? "))  
        if length<2 or length>20:
            print("Error message: wrong number")   
        else:
            words_list=get_words_from_file()    
            print(get_random_sentence(words_list,length))
    main()

# ========================Exercise 2: Working with JSON==================

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data=json.loads(sampleJson)

empl1=data["company"]["employee"]
salary=empl1["payable"]["salary"]
print(salary)

data["company"]["employee"]["birth_date"]="22.2.2222"
print(data)
json_sample=json.dumps(data)  
print(json_sample)                     