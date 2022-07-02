def well_defined(string):
    
    if "00" or "11" not in string:
        return True

    if '?' in string:
        for i in (len(string)):
            
            list1= string[:i] + '1' + string[:i+1]
            well_defined(list1)

            list2= string[:i] + '0' + string[:i+1]
            well_defined(list2)
    else:
        return False


print(well_defined('10?0'))

