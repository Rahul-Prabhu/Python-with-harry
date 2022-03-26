num=int(input("pl.enter the number:\n"))
list=[]
for i in range(1,11):
    list.append(i)
list.reverse()
print(list)
for i in list:
    print(f"{num}X{i}={num*i}")