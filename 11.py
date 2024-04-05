n=int(input("enter a number"))
sum=0
m=0
temp=n
while(n!=0):
 m=n%10
 sum=sum+m*m*m
 n=n//10
if(sum==temp):
    print("armstrong number")
else:
    print("not armstrong number")
