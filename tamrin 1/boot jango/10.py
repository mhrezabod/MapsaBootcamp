

message="Babak Khorramdin"
# alef
print (message[0])
# Be
print(message[6])
# pe
print(message[0:5])
print(message[6:16])
# te
print(message[:12:2])

# dal  
for i in range (len(message)-1):
    if message[i+1]== message[i]:
        print("mosavi")        
    else:
        print("namosavi")

for i in message:
    if i=="m":
        print("true")
        break