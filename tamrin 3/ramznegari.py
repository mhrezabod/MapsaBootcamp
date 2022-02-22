
def encryption (str: str, key:int):
    
    
    list_number=[ord(ch) for ch in str]
    temp_key_changed=[]
    for i in list_number:
        i=i+key
        temp_key_changed.append(i)

    temp_encrypted=[]
    for j in temp_key_changed:
        temp_encrypted.append(chr(j))
    temp_encrypted=''.join(temp_encrypted)

    return temp_encrypted

print(encryption('abc',3))


def decryption(str:str , key:int):

    list_number=[ord(ch) for ch in str]
    temp_key_changed=[]
    for i in list_number:
        i=i-key
        temp_key_changed.append(i)

    temp_decrypted=[]
    for j in temp_key_changed:
        temp_decrypted.append(chr(j))
    temp_decrypted=''.join(temp_decrypted)

    return temp_decrypted

print(decryption ("def",3))