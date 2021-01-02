import tools.helper as helper

def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')


def multiply_and_shift(char, a, b):    
    c = ord(char) - 65
    r = (a*c + b) % 26
    return (chr(r + 65))

def encrypt(message, key):
    multiply = key[0]
    add = key[1]

    ciphertext = ''
    for character in message:
        ciphertext += multiply_and_shift(character, multiply, add)
    
    return ciphertext

def solve():
    ciphertext = read_puzzle()


    plaintext = ''
    # Some helper functions you may find useful!
    x = helper.score_english(ciphertext, True)


    return plaintext

if __name__ == '__main__':
    print(solve())


