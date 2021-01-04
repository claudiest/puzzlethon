import tools.helper as helper

def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')

def shift_char(character):
    '''
    This one is a little different. (: 
    '''
    c = ord(character) - 65
    r = c + c % 26
    return (chr(r + 65))

def encrypt(message, substitution_table, shift_key):
    '''
    This will definitely fool them
    '''
    ciphertext = ''
    for character in message:
        encrypt_character = character

        # First scramble the character
        encrypt_character = shift_key(encrypt_character)

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