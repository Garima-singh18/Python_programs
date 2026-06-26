for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)

#print the multiplication table of a number n
n = int(input("enter number:"))
for i in range(1,11):
    print(n*i)

#find the sum of first natural numbers(using while)
n = 5
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
    print("sum =",sum)

#factorial number
n = 5
fact = 1
i = 1
while i<=n:
    fact*=i
    i+=1
    print("factorial=",fact)

n = 5
fact = 1
for i in range(1,n+1):
    fact*=1
    print("factorial=",fact)