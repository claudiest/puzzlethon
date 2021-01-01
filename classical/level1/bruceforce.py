def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')

def write_line_to_file(line):
    '''
    Writes out any line to scratchpad.txt
    '''
    with open('scratchpad.txt', 'a') as fd:
        # Add two newline characters for clarity
        fd.write(line + '\n' + '\n')

def char_shift(char, shift):
    '''
    Shifts the character RIGHT by shift amount.
    e.g. char_shift('A', 1) --> 'B'
    '''    
    # Re-index char (unicode)
    index = ((ord(char) - 65) + shift) % 26
    return (chr(index+65))

def encrypt(message, key):
    '''
    Function body for encryption.
    Hope it helps!
    '''
    ciphertext = ''
    for character in message:
        ciphertext += char_shift(character, key)

    return ciphertext

def solve():
    '''
    Function body. Look for the,
    # Write your code here! #
    '''

    # Read in the challenge
    ciphertext = read_puzzle()

    plaintext = ''
    # Write your code here! #

    return plaintext

if __name__ == '__main__':
    print(solve())