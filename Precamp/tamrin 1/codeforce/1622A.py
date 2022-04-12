numberOfinput = int(input())
for i in range(numberOfinput):
    x = input().split()
    l1 =int(x[0])
    l2 =int(x[1])
    l3 =int(x[2])
    stick=[l1,l2,l3]
    stick.sort()
    if stick[0]+stick[1]==stick[2]:
        print("YES")
    elif l1==l2 or l1==l3 or l2==l3:
        if stick[1]==stick[0]:
            if stick[2]%2==0:
                print('YES')
            else:
                print('NO')
        elif stick[1]==stick[2]:
            if stick[0]%2==0:
                print('yes')
            else:
                print('NO')
    else:
        print('NO')
