minimum = int(input("Enter the minimum number:"))
maximum = int(input("Enter the maximum number:"))
for number in range(minimum,maximum+1):
    count=0
    for i in range(2,(number//2+1)):
        if(number % i==0):
            count = count+1
            break
    if (count==0 and number!=1):
        print("%d" %number,end= ' ')
        
