n=121
m=0
sum=0
temp=n
while(n!=0):
   m=n%10
   sum=sum*10+m
   n=n//10
if(sum==temp):
     print("palimdrome")
else:
     print("not palindrome")
