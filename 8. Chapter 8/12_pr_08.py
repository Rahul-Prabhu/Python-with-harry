def mul(num,i):
    return num*i
num=int(input("pl.enter a no:\n"))
for i in range(1,11):
    print(f"{num} X {i} = {mul(num,i)}")