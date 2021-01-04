import tools.helper as helper

def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')

def encrypt(message, substitution_tables):
    ciphertext = ''
    plaintext = message

    for character in message:

        encrypt_character = character

        for table in substitution_tables:
            if encrypt_character in table:
                encrypt_character = table[encrypt_character]
            else:
                encrypt_character = encrypt_character 

        ciphertext += encrypt_character

    return ciphertext

def solve():
    puzzletext = read_puzzle()

    