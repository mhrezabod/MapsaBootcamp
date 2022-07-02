k = int(input())
list_ = (input().split())

set1=set()
set2=set()
for i in list_:
    if i in set1:   
        set2.add(i)
    else:
        set1.add(i)
capitan_room=list(set1.difference(set2))
print((capitan_room[0]))