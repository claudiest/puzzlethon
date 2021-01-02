import tools.helper as helper
def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')



def encrypt(message, substitution_table):
    '''
    Encrypts a message according to the substitution table you give it.
    If the substitution table isn't complete, don't change the character
    '''
    ciphertext = ''
    for character in message:
        try:
            ciphertext += substitution_table[character]
        except KeyError:
            ciphertext += character

def solve():
    ciphertext = read_puzzle()

    # Some helper tools you may find useful!
    helper.print_puzzle_stats(ciphertext)
    substitution_table = helper.SubstitutionTable()
    # You can add a pair of letters into the table like this
    substitution_table.add_pair('A', 'B')

    plaintext = ''


    return plaintext

    

if __name__ == '__main__':
    solve()