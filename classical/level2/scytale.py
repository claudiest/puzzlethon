import helper
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
    Encryption algorithm, hope this helps. 
    You can also see PUZZLEREADME.md for an explanation!
    '''
    ciphertext = ''
    mi = 0
    for i in range(len(message) * diameter):
        if i % diameter == 0:
            ciphertext += message[mi]
            mi += 1
        else:
            ciphertext += random_character()

    return ciphertext



def solve():
    ciphertext = read_puzzle()

    print_puzzle_stats(ciphertext)
    plaintext = ''



    return plaintext


if __name__ == '__main__':
    print(solve())
