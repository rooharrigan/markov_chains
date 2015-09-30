import random
from sys import argv
file_path = argv[1]

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_string = open(file_path).read()
    return text_string


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    n = int(raw_input("How long do you want your Markov chain keys to be?: "))

    words = text_string.split()
    for index in range(len(words)-2):
        # key = []
        # for i in range(n):
        #     key.append(words[i])
        # print key
        # break

        key = (words[index], words[index+1])
        word = words[index+2]
        if key in chains:
            chains[key].append(word)
        else:
            chains[key] = [word]

    return chains


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

# Produce random text
random_text = make_text(chains)

print random_text
