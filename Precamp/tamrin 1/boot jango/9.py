txt=""
i=0
for i in range(4):
    txt=txt+" "
i=0   
for i in range(5):
    txt=txt+"*"
print(txt)    
txt=""
i=0
for i in range(3):
    for j in range(3-i):
        txt=txt+" "
    txt=txt+"*"    
    for k in range(3):
        txt=txt+" "     
    txt=txt+"*" 
    print(txt)
    j=0
    k=0
    txt=""

i=0    
for i in range(5):
    txt=txt+"*"
print(txt)