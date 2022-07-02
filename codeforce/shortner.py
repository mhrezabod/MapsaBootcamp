def shortner(number):

    number = str(number)
    list=[]
    for i in range (len (number)-1):

        transferd_number=str(int(number[i])+int(number[i+1]))
        list.append(int(number.replace(number[i:i+2],transferd_number)))

    return max(list)


if __name__== "__main__" : 

    print(shortner(10038))