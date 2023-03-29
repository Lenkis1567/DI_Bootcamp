word_inp = input("please, write a word: ")
final_list = {}
i=0
for n in word_inp:
    if n not in final_list.keys():
        final_list[n]= [i]
    else:
        final_list[n].append(i)
    i +=1
print (final_list)


# ___________________________________________

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
# wallet = "$300"