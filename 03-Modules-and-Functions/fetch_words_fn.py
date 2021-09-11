#!/usr/bin/env python3
# Above line is called a Whole Shebang
# Shebang: Allows program loader to identify which interpreter to be used to run the program
#           It also conviniently documents if the program is python3 or python2
#
# On Mac/Linux - we need to mark our program permission to execute using chmod as shown below
#   chmod +x fetch_words_fn.py
#
# Once you do that you can run your programs without mentioning the python3 command as Shebang loads the correct interpreter, like below (both on linux and windows)
#   ./fetch_words_fn.py 'http://sixty-north.com/c/t.txt'
#
# On Windows => It uses and executable called PyLauncher (py.exe) to load the correct interpreter based on your Shebang. 
# And hence executing the above command as it is on Windows also works, despite Shebang given above is in unix format beyond python 3.3 onwards

# For Advanced command line argument parsing refer to
# Python Standard Library: argparse OR
# Third party options such as docopt

""" Retrieve and print words from a URL.

Usage:
    python3 fetch_words_fn.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url): #'http://sixty-north.com/c/t.txt'
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document
    
    Returns:
        A list of strings containing the words from the document
    """ #Docstring format

    #using with statements avoids resource leaks
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        items: An iterable series of printable items
    
    Returns:
        None
    """ #Docstring format    

    for item in items:
        print (item)


def main(url):
    """Print each word from a text document

    Args:
        url: The URL of a UTF-8 text document
    
    Returns:
        None
    """ #Docstring format    

    story_words = fetch_words(url)
    print_items (story_words)    


if __name__ == "__main__":
    main(sys.argv[1]) #The 0th argument is the module filename