import tools.helper as helper
import random

def random_character():
    '''
    Returns a random uppercase character
    '''
    r = random.randint(0, 25)
    return (chr(r + 65))

def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')

def encrypt(message, diameter):
    '''
    Encrypts a message on a 'scytale' with a variable diameter
    '''
    
    plaintext = message
    ciphertext = ''

    # Pad the message so it is the right length to be wrapped perfectly around the "rod"
    while len(plaintext) % diameter != 0:
        plaintext += random_character()
    
    # Create the "rod"
    row_length = len(plaintext) // diameter
    rod_rows = [' '] * diameter

    # Write the message aross the rod's rows
    mi = 0
    for i in range(0, diameter):
        rod_rows[i] = plaintext[mi:mi+row_length]
        mi += row_length
    
    # Create the ciphertext by reading the message vertically from the rows
    for i in range(0, row_length):
        for j in range(0, diameter):
            ciphertext += rod_rows[j][i]
        

    return ciphertext


def solve():
    ciphertext = read_puzzle()

    helper.print_puzzle_stats(ciphertext)
    plaintext = ''



    return plaintext


if __name__ == '__main__':
    print(solve())
