import random

def anagramize(raw_string):
    temp_string = []
    return_string = ''

    temp_string = list(raw_string)
    for char in range(len(temp_string)):
        number = random.randint(0, (len(temp_string) - 1))
        return_string += temp_string[number]
        temp_string.pop(number)

    return return_string

scrambles = 0
get_string = input('Enter text to scramble: ')
record = {}
while 1 == 1:
    run_again = 'no'
    anagram = anagramize(str(get_string))
    scrambles += 1
    results = 'Processed text: ' + anagram
    record.update({scrambles: anagram})
    print('\033[1A' + results + '\033[K')
    run_again = input('Press Enter to run again, input a character to quit. ')
    if run_again == '':
        continue
    else:
        break

print('You scrambled {} to {} in {} tries.'.format(get_string, anagram, scrambles))
