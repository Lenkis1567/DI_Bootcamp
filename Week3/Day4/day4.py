from collections import Counter
with open('starwars.txt', 'r') as file:
    text=file.read()
    text_list=text.split('\n')
    lines=text_list
    print(text)
   
    file.seek(0)
    print("Fifteen symbols: ", file.read(15))
    file.seek(0)
    print(file.readline(20))

    file.seek(0)
    text_list = file.readlines()
    print("List of strings:", text_list)
    print("Quantity of strings ", len(text_list))
    # dup = {x for x in text_list if text_list.count(x) > 1}
    # print(dup)

    file.seek(0)
    for _ in range(20):
        line=file.readline()
        print(line)
        if line =='':
            break

    file.seek(0)
    for n in range(20):
        line_n=file.readline()
        print(f"line {n}", line_n)
        if line_n =='':
            break

    luke = 0
    darth = 0
    lea = 0

    for word in text_list:
        word = word.strip('\n')
        if word == 'Luke':
            luke+=1
        if word == 'Lea':
            lea+=1
        if word == 'Darth':
            darth+=1
    print("Lea quantity: ", lea)
    print("Darth quantity: ", darth)
    print("Luke quantity: ", luke)  
    # or
    # 
    #          
    # print("Lea quantity: ", text_list.count("Lea\n"))
    # print("Darth quantity: ",text_list.count("Darth\n"))
    # print("Luke quantity: ",text_list.count("Luke\n")+1)

    # or
    file.seek(0)
    text=file.read()
    text_list=text.split("\n")
    list=text_list
    print(Counter(list))

    to_append = '\nElena'
with open('starwars.txt', 'a') as file:
    file.write(to_append)
    lines_updated =[]
    new_line="Luke Sky"
    for line in list:
        if line=="Luke":
            new_line=line
        list.append(new_line)

# ==================================================
