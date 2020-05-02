#!/usr/bin/env python

from collections import defaultdict

import random
import string
import sys
import unicodedata

if sys.version_info.major < 3:
    sys.exit("Error: this script requires Python version 3")

class TextStyler:
    def __init__(self):
        self.__charmap = defaultdict(list)
        self.__build_char_mapping()

    def convert(self, text):
        """
        Convert all ascii alphanumeric characters to random stylish unicode
        characters.
        """
        converted = list()
        for ch in text:
            stylish_ch = random.choice(self.__charmap.get(ch, [ch]))
            converted.append(stylish_ch)

        return "".join(converted)

    def __build_char_mapping(self):
        """
        Build a dictionary (char -> list of char).
        Each key maps a list of equivalent similar looking characters.
        Keys are from ascii alphnumeric range.
        """
        valid_chars = string.ascii_letters + string.digits

        # Unicode Mathematical Alphanumeric Symbols block range
        start = 0x1D400
        end = 0x1D7FF

        for ch in range(start, end+1):
            n = unicodedata.normalize('NFKD', chr(ch))
            if n in valid_chars:
                self.__charmap[n].append(chr(ch))


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        sys.exit('Usage: {} "<text>"'.format(sys.argv[0]))

    text = "".join(sys.argv[1:])
    styler = TextStyler()
    print(styler.convert(text))

    sys.exit(0)
