n=int(input("enter a number"))
sum=0
m=0
while(n!=0):
 m=n%10
 sum=sum*10+m
 n=n//10
print(sum)
