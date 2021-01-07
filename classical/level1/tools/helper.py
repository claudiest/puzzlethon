def write_line_to_file(line):
    '''
    Writes out any line to scratchpad.txt
    '''
    with open('scratchpad.txt', 'a') as fd:
        # Add two newline characters for clarity
        fd.write(line + '\n' + '\n')


class TextAnalyser:
    '''
    Class skeleton for the extension exercise
    '''
    corpus = []

    def __init__(self, dictionary_file):
        self.create_corpus(dictionary_file)
    
    def create_corpus(self, dictionary_file):
        with open(dictionary_file) as fd:
            # Best not load the whole file into memory
            for line in fd:
                self.corpus.append(line)
    
    def english_words(self, text):
        '''
        Given a piece of text, can you determine how many dictionary words are present?
        '''
        # You can access the list of words using the list, self.corpus 

        num_words = 0
        return num_words