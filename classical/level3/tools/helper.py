
class SubstitutionTable(dict):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, *args, **kwargs):
        super(SubstitutionTable, self).__init__(*args, **kwargs)
        self.__dict__ = self
        self.reset_table()

    def reset_table(self):
        for letter in self.alphabet:
            self.__dict__ [letter] = letter 
        
    def add_pair(self, p1, p2):
        p1,p2 = p1.upper(), p2.upper()

        # Remove letters from the table if they already exist
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
    
    def print_table(self):
        '''
        Prints out your table to the screen
        '''
        print ("Substitution Table")
        print ("---")
        for key in list(self.__dict__.keys()):
            print("{} --> {}".format(key, self.__dict__[key]))


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
    
    print ("\n")