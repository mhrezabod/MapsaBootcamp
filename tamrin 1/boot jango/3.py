a = int(input('enter a number : '))
b = int(input('enter a number : '))
c = int(input('enter a number : '))

if a> b and c:
    print("max is : ",a)
    if b>c:
        print('min is :',c)
    else:
        print('min is :',b)
elif b > a and c:
    print("max is : ",b)
    if a>c:
        print('min is :',c)
    else:
        print('min is :',a)
elif print("max is : ",c):
    if a>b:
        print('min is :',b)
    else:
        print('min is :',a)
else:
    print("enter the right numbers again!")