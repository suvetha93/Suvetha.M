nterms = int(input("how many  terms you want?"))

# first two terms
n1 = 0
n2 = 1
count = 2
if nterms <= 1:
    print("enter the positive integer")
elif nterms == 1:
    print("fibonacci sequences:")
    print(n1)
else:
    print("fibonacci sequences:")
    print(n1,",",n2,end=',')
    while count < nterms:
        nth = n1 +  n2
        print(nth,end=',')

        #update values

        n1 = n2
        n2 = nth
        count +=1
