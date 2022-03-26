# n = int(input().strip())

# x,y,z = map(str, input().rstrip().split())
# print(x+y+z)
# if x=="rahul":
#     print(x)
# else:
#     print("not rahul")
import numpy
l=[]
n,m=map(int,input().split())
for i in range(n):
    l.append(list(map(int,input().split())))
my_array=numpy.array(l)
print(my_array)
arr=numpy.sum(my_array,axis=0)
x=1
for i in range(len(arr)):
    x=x*arr[i]
print(x)
    