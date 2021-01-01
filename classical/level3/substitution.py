class SubstitutionTable(dict):

    def __init__(self, *args, **kwargs):
        super(SubstitutionTable, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def add_pair(self, p1, p2):
        # Remove letters if they already exist
        if p1 in self.__dict__:
            pair_del = self.__dict__[p1]
            del self.__dict__[p1]
            del self.__dict__[pair_del]
                    
        if p2 in self.__dict__:
            pair_del = self.__dict__[p2]
            del self.__dict__[p2]
            del self.__dict__[pair_del]

        # Pair letters
        self.__dict__[p1] = p2 
        self.__dict__[p2] = p1


def print_puzzle_stats(puzzletext):
    '''
    Provides stats about the puzzle you may find useful!
    '''
    freq_dict = {}
    length = len(puzzletext)

    # Get frequency
    for c in puzzletext: 
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1
    
    # Normalise
    for key in freq_dict.keys():
        freq_dict[key] = freq_dict[key] / length

    # Print
    print("Length : {}".format(length))
    print("Frequency of Characters")
    print("---")

    for key in freq_dict.keys():
        print("{} : {}".format(key, freq_dict[key]))



def read_puzzle():
    '''
    Reads in file from puzzle.txt
    '''
    with open('puzzle.txt', 'r') as fd:
        s = fd.read()

    # clean up newlines just in case
    return s.replace('\n', '')



def encrypt(message, substitution_table):
    ciphertext = ''
    for character in message:
        ciphertext += substitution_table[character]

def solve():
    ciphertext = read_puzzle()


    print_puzzle_stats(ciphertext)
    substitution_table = SubstitutionTable()

if __name__ == '__main__':
    solve()