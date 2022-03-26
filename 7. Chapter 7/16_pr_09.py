num=int(input("pl. enter the no. :\n"))
sum=0
for i in range(1,num+1):
    sum=sum+i
avg=sum/num

for i in range(1,num+1):
    if i != avg :
        print("*"*(num))
    else:
        for j in range(1,num+1):
            if j != avg :
                print("*",end="")
            else:
                print(" ",end="")
        print("")
     