for i in range (1,11):
    for j in range (1,11):
        multi=i*j
        if multi<10:
            space='  '
        else:
            if multi<100:
                space=' '
        print(space,multi,end='')
    print()
    