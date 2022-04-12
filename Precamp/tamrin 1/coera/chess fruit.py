from unittest import result


def fruits(_fruits):
    result={}
    for i in range(len(_fruits)):
        if _fruits[i]['shape']=='sphere': 
           if _fruits[i]['mass'] in range (300,601):
               if _fruits[i]['volume'] in range (100,501):
                   if _fruits[i]['name'] in result:
                       result[_fruits[i]['name']]+=1
                   else:
                       result[_fruits[i]['name']]=1
    return result
