#EVEN MORE PRACTICE


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word afeter popping if off."""
    word = words.pop(0)
    print(word)
    
def print_last_word(words):
    """Prints the last word after poopping it of"""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """Prints the first and last words of the sentence."""
    word = break_words(sentence)
    return sort_words(word)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentences"""
    words = break_words(sentence)
    print_first_word()
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    