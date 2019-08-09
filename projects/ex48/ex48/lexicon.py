lexicon ={
    "north":"direction",
    "south":'direction',
    'east':'direction',
    'west':'direction',

    'go':'verb',
    'kill':'verb',
    'eat':'verb',
    'run':'verb',

    'the':'stop',
    'in':'stop',
    'of':'stop',

    'bear':'noun',
    'IAS':'error',
    'princess':'noun',

    'ASDFAFSSD':'error'
}

def scan(sentence):
    results = []
    words = sentence.split()

    for word in words:
        try:
            results.append(('number',int(word)))
        except ValueError:
            word_type = lexicon.get(word)
            results.append((word_type,word))
    return results
