# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n
def add(n):
    if n==0:
        return 0
    else:
        return n + add(n-1) 
n=int(input("pl.enter the number:\n"))
print("The sum of first "+str(n)+" natural number is " + str(add(n)))
