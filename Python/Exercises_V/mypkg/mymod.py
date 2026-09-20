"""

Call the script from the command line and add the file name after the name of the script
or import the script.

"""

import sys

# Note, it seems I don't need to close the file before reading it again.
# So I could shorten the functions.

def countLines(name):
    f = open(name, 'r')
    # res = len(f.readlines())
    # f.close()
    return len(f.readlines())

def countChars(name):
    f = open(name, 'r')
    # res = len(f.read())
    # f.close()
    return len(f.read())

def test(name):
    print('Number of Lines = ', countLines(name)) 
    print('Number of Characters = ', countChars(name)) 

# The code below allows to use the script interactively or to import it in another script.
# It's important to use __main__ not just main

if __name__ == '__main__':     
    test(sys.argv[1])