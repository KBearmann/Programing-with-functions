import random

def main():
    # Generate and print sentences with the required characteristics
    sentences = [
        make_sentence('single', 'past'),
        make_sentence('single', 'present'),
        make_sentence('single', 'future'),
        make_sentence('plural', 'past'),
        make_sentence('plural', 'present'),
        make_sentence('plural', 'future')
    ]
    
    for sentence in sentences:
        print(sentence)

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner} {noun} {verb} {prepositional_phrase}."
    return sentence.capitalize()

def get_determiner(quantity):
    if quantity == 'single':
        determiners = ['a', 'one', 'the']
    else:
        determiners = ['some', 'many', 'the']
    return random.choice(determiners)

def get_noun(quantity):
    if quantity == 'single':
        nouns = ['boy', 'dog', 'girl', 'man', 'woman', 'cat']
    else:
        nouns = ['boys', 'dogs', 'girls', 'men', 'women', 'cats']
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

def get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

main()
