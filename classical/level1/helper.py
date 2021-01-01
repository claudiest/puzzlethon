def write_line_to_file(line):
    '''
    Writes out any line to scratchpad.txt
    '''
    with open('scratchpad.txt', 'a') as fd:
        # Add two newline characters for clarity
        fd.write(line + '\n' + '\n')