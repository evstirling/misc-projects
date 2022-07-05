import random

encrypt_key = []
scramble_key = []

def add_keys(key1, key2, string):
    key_string1 = ''
    key_string2 = ''

    for entry in range(len(key1)):
        key_string1 += str(key1[entry])
    for entry in range(len(key2)):
        key_string2 += chr((key2[entry] - 64) % (90-65) + 64)
    
    template = [key_string2, string, key_string1]
    return ' || '.join(template)

def encrypt(string):
    global encrypt_key

    new_string = ''
    counter = 0

    for char in string:
        key = int(random.randint(10, 99))
        encrypt_key.append(key)
        counter += 1
        if counter % 2 == 0:
            character = (chr((ord(char) + key - 32) % (126-33) + 32)) 
        else:
            character =  (chr((ord(char) - key - 32) % (126-33) + 32))  
        new_string += character

    return new_string

def scramble(string):
    global scramble_key

    temp_string = []
    return_string = ''

    temp_string = list(string)
    for char in range(len(temp_string)):
        number = random.randint(0, (len(temp_string) - 1))
        scramble_key.append(number)
        return_string += temp_string[number]
        temp_string.pop(number)

    return return_string

def mode_encrypt():       
    string_in = input('Enter string: ')
    string_en = encrypt(string_in)
    string_scram = scramble(string_en)
    string_out = add_keys(encrypt_key, scramble_key, string_scram)
    print(string_out)

mode_encrypt()