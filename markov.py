import random
from sys import argv
file_path = argv[1]

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()
    return text_string


def make_chains(text_string):
    """Takes input as text string, returns dictionary or Markov chains"""
    chains = {}
    n = int(raw_input("Length of Markov chains: "))
    
    #Split out the text string into a list of words
    words = text_string.split()

    #Make a key out of the text string that is n letters long
    i = 0

    while i < len(words) - (n+1):
        print words
        key = words[i:n+i]
        print key
        value = words[i+n]
        print value
        key = tuple(key)

    #check is the key is in the dictionary, or put it in
        if key not in chains:
            chains[key] = []
            chains[key].append(value)
        else:
            chains[key].append(value)
        i += 1
        print i
    print chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    key = random.choice(chains.keys())
    text = (' ').join(key)

    while key in chains.keys():
        val_list = chains[key]
        word3 = random.choice(val_list)
        text = text + ' '+ word3
        key = (key[1], word3)

    return text

# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
