list_1 = [1,8,10,15,12,19, 12]
list_2 = []
a=input("insert number :")
a_num = int(a)
item=input("insert item:")
for i in range(0, len(list_1)+1):
    if i < (a_num-1):
        list_2.append(list_1[i])
    if i == (a_num-1):
        list_2.append(item)    
    if i > (a_num-1):
        list_2.append(list_1[i-1])
print(list_2)
