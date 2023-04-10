string_cars="Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
list_cars=string_cars.split(',')
print(list_cars)
print(f'Here are {len(list_cars)} munifactuters.')
list_cars.sort(reverse=True)
print("Reserse sorted: ", list_cars)
o="o"
o_list=[x for x in range(0, len(list_cars)) if o in list_cars[x]]
print("here are the numbers of words, where there is 'o':",o_list,", here is the quantity of the words: ", len(o_list))

i_list=[x for x in range(0, len(list_cars)) if "i" in list_cars[x]]
print("here are the numbers of words, where there is 'i':",i_list,", here is the quantity of the words with it: ", len(i_list))

list_cars_dupl = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
list_cars_dupl_w=set(list_cars_dupl)
list_cars_dupl_ws=str(list_cars_dupl_w)
list_cars_dupl_list=list(list_cars_dupl_w)
print(list_cars_dupl_ws)
list_reverse=[]
for b in range(0, len(list_cars_dupl_list)):
    res = ''.join(reversed(list_cars_dupl_list[b]))
    list_reverse.append(res)

print(list_reverse)

# list_cars_dupl_w = [list_cars_dupl[] for a in range(0, len(list_cars_dupl)) if list_cars_dupl[a] not in list_cars_dupl_w]

