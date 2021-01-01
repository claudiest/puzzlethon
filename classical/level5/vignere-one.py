def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')

def add_chars(char1, char2):
    '''
    Shifts the first character right by the second character
    e.g. add_chars('A', 'B') = 'A' + 'B' --> 'C' 
    '''    
    # convert characters to integers
    c1 = ord(char1) - 65
    c2 = ord(char2) - 65
    r = c1 + c2 % 26
    return (chr(r+65))

def encrypt(message, key):
    
    keylength = 4
    ki = 0
    ciphertext = ''
    for character in message:
        ciphertext += char_shift(character, key[ki])
        ki = (ki + 1) % keylength
    
    return ciphertext

def solve():
    ciphertext = read_puzzle()


    # Your Code Here! #
    plaintext = ''


    return plaintext

if __name__ == '__main__':
    print(solve())