import re

T = int(input())
list1=[]
for i in range (T):
    list1.append(input())
    
for j in list1:
    try:
        re.compile(j)
        print(True)
  
    except re.error:
        print(False)