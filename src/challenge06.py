#!/usr/bin/env python3

import sys
import base64
import codecs
import binascii
from errors import *

def main():
	try:
		file = checkFile(6)
		str = file.read()
		# str = str.rstrip("\r\n"))
		result, key = break_key(base64.b16decode(str))
		# str = base64.b64encode(str)
		# result, key = break_key(base64.b64decode(str))
		# result, key = break_key(codecs.encode(codecs.decode(str, 'hex'), 'base64'))
		# print("%d\n",bin(int(str, 16))[2:].zfill(8))
		# print("%d", codecs.encode(codecs.decode(str, 'hex'), 'base64'))
		k1 = key[round(len(key)/2):]
		k2 = key[:round(len(key)/2)]
		if (hamming(k1,k2) == 0):
			print(k1.hex().upper())
		else:
			print(key.hex().upper())
		# print("Key: {}\nMessage: {}".format(key.hex(), result))
	except ValueError:
		fileError()

def break_key(text):
	# text = str(text)
	m_distances = []
	for keysize in range(5, 41):
		distances = []
		blocks = [text[i:i + keysize] for i in range(0, len(text), keysize)]
		while True:
			try:
				b1 = blocks[0]
				b2 = blocks[1]
				distances.append(hamming(b1, b2)/keysize)
				del blocks[0]
				del blocks[1]
			except Exception as e:
				break
		result = {
			'key': keysize,
			'dist': sum(distances)/len(distances)
		}
		m_distances.append(result)
	key_lengths = sorted(m_distances, key=lambda x: x['dist'])[0]
	plaintext = []

	key = b''
	key_length = key_lengths['key']
	for i in range(key_length):
		block = b''
		for j in range(i, len(text), key_length):
			block += bytes([text[j]])
		key += bytes([simple_single_xor(block)['key']])
	plaintext.append((repeating_key_xor(text, key), key))
	return max(plaintext, key=lambda x: scoring(x[0]))

def repeating_key_xor(message_bytes, key):
	output_bytes = b''
	index = 0
	for byte in message_bytes:
		output_bytes += bytes([byte ^ key[index]])
		if (index + 1) == len(key):
			index = 0
		else:
			index += 1
	return output_bytes

def simple_single_xor(hex):
	messages = []
	for key in range(256):
		message = single_xor(hex, key)
		score = scoring(message)
		data = {
			'message': message,
			'score': score,
			'key': key,
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


def hamming(s1, s2):

	dist = 0
	if (len(s1) != len(s2)):
		return 0
		# s2 = pad(s2, len(s1))
		# return (len(s1) - len(s2))
	for b1, b2 in zip(s1, s2):
		diff = b1 ^ b2
		dist += sum([1 for bit in bin(diff) if bit == '1'])

	return dist

def pad(input, size):
	if len(input) == size:
		return input
	padding_length = size - len(input) % size
	padding = bytes([padding_length] * padding_length)
	return (input + padding)


toHex = lambda x:"".join([hex(ord(c))[2:].zfill(2) for c in x])

if __name__ == "__main__":
	main()