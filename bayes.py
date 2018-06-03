import numpy as np
import string

file = open('trainingSet.txt')

vocabulary = []

for line in file:
	# Tokenize the line
	buffer = line.split()
	
	for object in buffer:
		# Strip punctuation
		object = object.translate(None, string.punctuation)
		if object not in vocabulary:
			vocabulary.append(object)

# Alphabetize
vocabulary.sort()

out  = open("preprocessed_train.txt","w")
# Write vocab to file
for word in vocabulary:
	out.write(str(word))
	out.write(",")

out.write("classlabel\n")

#	Generate Feature Set
for line in file:
	buffer = line.spit()

file.close()
