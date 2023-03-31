# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
str_words="without,hello,bag,world"
print (str_words)
list_words = str_words.split(",")
print (list_words)
list_words.sort()
str=", ".join(list_words)
print(str)

