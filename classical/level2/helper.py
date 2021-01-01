def print_puzzle_stats(puzzletext):
    '''
    Gives you some observations on the puzzle that you may find useful!
    '''
    print("Length : {}".format(len(puzzletext)))

def write_line_to_file(line):
    '''
    Writes out any line to scratchpad.txt
    '''
    with open('scratchpad.txt', 'a') as fd:
        # Add two newline characters for clarity
        fd.write(line + '\n' + '\n')