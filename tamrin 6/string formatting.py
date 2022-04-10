def print_formatted(number):
    space = number.bit_length()
    for i in range(1, number+1):
        print(f"{i:{space}d} {i:{space}o} {i:{space}X} {i:{space}b}")

print_formatted(17)