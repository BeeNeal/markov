"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text_file:
        long_text = text_file.read()
        #long_text = long_text.replace("\n", " ")
        #words = long_text.split()

    return long_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()  # creates list from text_string
    words.append(None)  # add none at end of list to indicate stopping point

    #Looping through up and including last pair
    for i in range(len(words)-2):
        state = (words[i], words[i + 1])  # creates tuple of bigram
        transition = words[i + 2]  # creates value of word following bigram
        chains[state] = chains.get(state, [])  # checks if bigram in dict, creates empty list if not
        chains[state].append(transition)  # adds to transition list

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    start_key = choice(chains.keys())
    words.extend(start_key)
    new_key = start_key

    while True:
        combo_list = chains[new_key]
        transition = choice(combo_list)

        if transition is None:
            break

        words.append(transition)
        new_key = (new_key[1], transition)

        # if new_key not in chains:
        #     break

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
