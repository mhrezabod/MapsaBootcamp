n , m = (input('please enter n & m : ').split())
N= input('enter the array: ').split()

A = set(input().split())
B = set(input().split())
happines=0

for i in N:
    if i in A:
        happines+=1
    if i in B:
        happines-=1
print(happines)
