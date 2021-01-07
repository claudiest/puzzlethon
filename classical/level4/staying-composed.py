import tools.helper as helper

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

def encrypt(message, substitution_table, caesar_key):
    '''
    This will definitely fool them
    '''
    ciphertext = ''
    for character in message:
        encrypt_character = character

        # First scramble the character
        encrypt_character = char_shift(encrypt_character, caesar_key)

        # Then pass it through the substitution table
        if encrypt_character in substitution_table:
            encrypt_character = substitution_table[encrypt_character]
        else:
            encrypt_character = encrypt_character
        
        ciphertext += encrypt_character
    
    return ciphertext

def solve():
    puzzletext = read_puzzle()



    # Your code here! #
    plaintext = ''   





    return plaintext



if __name__ == '__main__':
    print(solve())