def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')

def char_shift(char, shift):
    '''
    Shifts the character RIGHT by shift amount.
    e.g. char_shift('A', 1) --> 'B'
    '''

    if shift < 0:
        print("Haha, nice try. No negative numbers allowed!")
        return char

    # Re-index char (unicode)
    c = ((ord(char) - 65) + shift) % 26
    return (chr(c+65))

def encrypt(message):
    '''
    Function body for encryption.
    Hope it helps!
    '''
    ciphertext = ''
    for character in message:
        ciphertext += char_shift(character, 3)

    return ciphertext

def solve():
    '''
    Function body. Look for the,
    # Write your code here! #
    '''

    # Read in the challenge
    puzzletext = read_puzzle()

    plaintext = ''
    # Write your code here! #

    return plaintext


if __name__ == '__main__':
    print(solve())