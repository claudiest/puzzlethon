def write_line_to_file(line):
    '''
    Writes out any line to scratchpad.txt
    '''
    with open('scratchpad.txt', 'a') as fd:
        # Add two newline characters for clarity
        fd.write(line + '\n' + '\n')


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