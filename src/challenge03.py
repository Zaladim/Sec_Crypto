#!/usr/bin/env python3

import sys
import base64
import binascii
from errors import *

def main():
	try:
		messages = []
		file = checkFile(3)
		str = file.read()
		str = str.rstrip("\r\n")
		for i in range(256):
			text = single_xor(bytes.fromhex(str), i)
			score = scoring(text)
			data = {
				'text': text,
				'score': score,
				'key': i
			}
			messages.append(data)
		best_score = sorted(messages, key=lambda x: x['score'], reverse=True)[0]
		
		print('%x' % (best_score.get('key')))
		# print(hex(best_score.get('key')).lstrip("0x").upper())
	except ValueError:
		fileError()

def single_xor(input, char):
	output = b''
	for byte in input:
		output += bytes([byte ^ char])
	return output

def scoring(input):
	character_frequencies = {
		'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
		'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
		'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
		'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
		'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
		'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
		'y': .01974, 'z': .00074, ' ': .13000
	}
	return sum([character_frequencies.get(chr(byte), 0) for byte in input.lower()])


if __name__ == "__main__":
	main()