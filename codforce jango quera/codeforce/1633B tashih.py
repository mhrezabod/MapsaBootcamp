

def Minority(a):
    b = a.count('0')
    c = a.count('1')
    if b<c or b>c:
        mo=min(b,c)
    else:
        mo=int(len(a)/2)
    return mo

#print(Minority('1'))


for i in range(int(input())):
    s = input()
    print(s)
    print(min((len(s) - 1) // 2, s.count('0'), s.count('1')))