import random
x=random.randint(1,20)
y = int(input("yek adad hads bezanid: "))
msg= 'game over'

for i in range(4):
    if y!=x:
        print("wrong")
        y=int(input("yek adad digar hads bezanid: "))
    else:
        msg= 'you win!'
        break
print(msg)
print('random number is:',x)