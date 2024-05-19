import random

def main():
    # Generate and print sentences
    for _ in range(5):
        quantity = random.choice(['single', 'plural'])
        tense = random.choice(['past', 'present', 'future'])
        sentence = make_sentence(quantity, tense)
        print(sentence)

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner} {noun} {verb}."
    return sentence.capitalize()

def get_determiner(quantity):
    if quantity == 'single':
        determiners = ['a', 'one', 'the']
    else:
        determiners = ['some', 'many', 'the']
    return random.choice(determiners)

def get_noun(quantity):
    if quantity == 'single':
        nouns = ['boy', 'dog', 'girl', 'guy', 'woman', 'cat']
    else:
        nouns = ['boys', 'dogs', 'girls', 'guys', 'women', 'cats']
    return random.choice(nouns)

def get_verb(quantity, tense):
    if tense == 'past':
        if quantity == 'single':
            verbs = ['laughed', 'ate', 'drank', 'walked', 'thought', 'wrote']
        else:
            verbs = ['laughed', 'ate', 'drank', 'walked', 'thought', 'wrote']
    elif tense == 'present':
        if quantity == 'single':
            verbs = ['laughs', 'eats', 'drinks', 'walks', 'thinks', 'writes']
        else:
            verbs = ['laugh', 'eat', 'drink', 'walk', 'think', 'write']
    else:  # future
        verbs = ['will laugh', 'will eat', 'will drink', 'will walk', 'will think', 'will write']
    return random.choice(verbs)

main()