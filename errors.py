import sys
import os

def usage(n):
	print("USAGE: ./challenge0%d input0%d.txt" %(n, n))
	exit(84)

def fileError():
	print("ERROR: File not correct.")
	exit(84)

def isFileEmpty(filePath):
	if (os.stat(filePath).st_size == 0):
		print("ERROR: File shouldn't be empty.")
		exit(84)

def checkFile(n):
	if (len(sys.argv) != 2):
		usage(n)
	try:
		isFileEmpty(sys.argv[1])
		file = open(sys.argv[1], "r")

		return file
	except FileNotFoundError:
		usage(n)
	except PermissionError:
		fileError()