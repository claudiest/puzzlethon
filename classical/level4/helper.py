def score_english(puzzletext):
    '''
    This may take an extra second on older machines
    '''
    count = 0
    length = len(puzzletext)
    with open('../dictionary/dictionary.txt') as fd:
        for line in fd:
            word = line.strip()
            count += puzzletext.count(word)

    return (count / length)

