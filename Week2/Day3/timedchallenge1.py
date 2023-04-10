num=int(input('input the number: '))
delit=[1]
for i in range(2, num-1):
    if num%i==0:
        delit.append(i)
print(delit)
if num==sum(delit):
    print(f"{num} is the perfect number")
else:
    print(f"{num} is not perfect")
