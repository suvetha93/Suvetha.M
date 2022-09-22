n=int(input("Enter the number"))
c=1
for i in range(2,n):
    if n%i==0:
        c=0
if c==1:
    print("number is prime")
else:
    print("number is not prime")
