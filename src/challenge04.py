#!/usr/bin/env python3

import sys
import base64
from errors import *

def main():
	try:
		file = checkFile(4)
		lines = file.read().splitlines()
		text = []
		for i in range(len(lines)):
			hexstring = bytes.fromhex(lines[i])
			text.append(simple_single_xor(hexstring, i))
		best = sorted(text, key=lambda x: x['score'], reverse=True)[0]
		print(str(best.get('line')) + " " + hex(best.get('key'))[2:].upper())
	except ValueError:
		fileError()

def simple_single_xor(hex, line):
	messages = []
	for key in range(256):
		message = single_xor(hex, key)
		score = scoring(message)
		data = {
			'message': message,
			'score': score,
			'key': key,
			'line': line + 1
			}
		messages.append(data)
	return sorted(messages, key=lambda x: x['score'], reverse=True)[0]

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