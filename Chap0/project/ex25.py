def break_words(stuff):
    """This function will break up words for us."""
    # triple quotes turn to be the document of ex25 help
    words = stuff.split(' ')
    # listing the parts of breaking
    return words

def sort_words(words):
    """ Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    # remove the 1st word from the breaking list,so the listing got changed
    word = words.pop(0)
    # print out the 1st word that is no longer in the list.
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    # remove the last word,here the list got the same last one as of the print_first_word.
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # whats difference with break_words(words)? keep the unaffected data while the listing undergoes change.
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # the function with other functions.
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    # breaking,listing,sorting,removing,printing.
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
