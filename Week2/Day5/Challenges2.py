def selk1(n:int, level=1):
    if n>0:
        print(" "*n,"*"*(level))
        selk1(n-1, level+1)

selk1(5)

def selk(l:int):
    for i in range(1,l+1):
        print(" "*(l-i),"*"*i)

selk(3)

def simm(n:int, level = 1):
    if n>0:
        print(" "*(n-1)+"*"*(level*2-1))
        simm(n-1, level+1)
simm(10)        
# ===============================
def romb(n:int):
    for i in range(1, n):
        print("*"*i) 
    print("*"*i)
    for i in range(0, n):
        print(" "*(i), "*"*(n-i-2))
romb(10)

# ==============
my_list = [2, 24, 12, 354, 233, 450, 3, 7]
for i in range(len(my_list) - 1): 
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
# took list, 
# 1) i = 0 minimum = 0 (loop form 0 to n-1)
# 2) j = 1 (loop from 1 to n)
# 3) if list(1) <list(0)  -----  24<2
#       minimum = j (indext from min)
#   if minimum != i ------- > 0 = 0 
#       then change places
#repeat till the end