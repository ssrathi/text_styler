#!/usr/bin/env python

from text_styler import TextStyler

import random
import string
import sys

def test_styler(num=1, length=80):
	"""
	Test Styler code with given number of sentences of specified length.
	"""
	styler = TextStyler()
	sentences = __random_sentences(num=num, length=length)

	for sentence in sentences:
		print("Original : {}".format(sentence))
		print("Converted: {}".format(styler.convert(sentence)))
		print("")

def __random_sentences(num=1, length=80):
	"""
	Generate given number of random ASCII sentences with specified length.
	"""
	space_cnt = length//15
	letters = string.ascii_letters
	all_chars = letters + string.digits + ',.' + ' '*space_cnt

	sentences = list()
	for i in range(num):
		# Only use a letter at first position
		sentence = ''.join(random.choices(letters, k=1) +
				random.choices(all_chars, k=length-1))
		sentences.append(sentence)
	return sentences


if __name__ == "__main__":
	argc = len(sys.argv)
	if argc > 3:
		sys.exit("Usage: {} <num> <size>".format(sys.argv[0]))

	sentence_cnt = int(sys.argv[1]) if argc > 1 else 10
	sentence_size = int(sys.argv[2]) if argc > 2 else 80
	test_styler(num=sentence_cnt, length=sentence_size)

	sys.exit(0)
