def game(number):
    
    yekan=number%10
    dahgan=(number-yekan)/10
    if yekan>=dahgan:
        number=yekan-dahgan
    else:
        number=dahgan-yekan
    return(int(number))
