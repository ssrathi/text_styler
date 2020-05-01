# -*- encoding: utf-8 -*-

from collections import defaultdict

import random
import string
import sys
import unicodedata

def build_char_mapping():
    """
    Return a dictionary (char -> list of char).
    Each key maps a list of equivalent similar looking characters.
    Keys are from ascii alphnumeric range.
    """
    valid_chars = string.letters + string.digits
    
    # Unicode Mathematical Alphanumeric Symbols block range
    start = 0x1D400
    end = 0x1D7FF

    charmap = defaultdict(list)
    for ch in xrange(start, end+1):
        n = unicodedata.normalize('NFKD', unichr(ch))
        if n in valid_chars:
            charmap[n].append(unichr(ch))

    return charmap

def convert_text(text, charmap):
    """
    Convert all ascii alphanumeric characters to random stylish unicode
    characters.
    """
    converted = list()
    for ch in text:
        stylish_ch = random.choice(charmap.get(ch, [ch]))
        converted.append(stylish_ch)

    return "".join(converted)

def usage():
    print 'Usage: %s "<text>"' % sys.argv[0]

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        usage()
        sys.exit(-1)

    charmap = build_char_mapping()
    text = "".join(sys.argv[1:])

    stylished = convert_text(text, charmap)
    print stylished
    sys.exit(0)
