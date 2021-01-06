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
    If the substitution table doesn't have an entry for a character, character is unchanged
    '''
    ciphertext = ''
    for character in message:
        if character in substitution_table:
            ciphertext += substitution_table[character]
        else:
            ciphertext += character

    return ciphertext

def solve():
    puzzletext = read_puzzle()

    # Some helper tools you may find useful!
    helper.print_puzzle_stats(puzzletext)

    # You can use a standard dictionary if you like 
    # I've written this one in case you want to print out your table
    # e.g.
    # substitution_table = helper.SubstitutionTable()
    # substition_table.print_table()
    substition_table = helper.SubstitutionTable()
    substition_table.print_table()
    
    plaintext = ''



    return plaintext

    

if __name__ == '__main__':
    print(solve())