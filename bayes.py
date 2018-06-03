import numpy as np
import string

file = open('trainingSet.txt')

vocabulary = []

for line in file:
	# Tokenize the line
	buffer = line.split()
	
	for object in buffer:
		# Strip punctuation and make lower case
		object = (object.translate(None, string.punctuation)).lower()
		if object not in vocabulary:
			vocabulary.append(object)

# Alphabetize
vocabulary.sort()

for thing in vocabulary:
	print thing

file.close()