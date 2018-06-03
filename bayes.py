import numpy as np
import string

file = open('trainingSet.txt')
out  = open("preprocessed_train.txt","w")

vocabulary = []

for line in file:
	# Tokenize the line
	buffer = line.split()

	# Remove the classlabel
	buffer.pop(len(buffer)-1)
	
	for object in buffer:
		# Strip punctuation and make lower case
		object = (object.translate(None, string.punctuation)).lower()
		if object not in vocabulary:
			vocabulary.append(object)

# Alphabetize
vocabulary.sort()

# Write vocab to file
for word in vocabulary:
	out.write(str(word))
	out.write(",")

out.write("classlabel\n")

#	Generate Feature Set
file.seek(0)
for line in file:
	# Tokenize the line
	buffer = line.split()

	# Store the classlable and remove it from buffer
	value = buffer[len(buffer)-1]
	buffer.pop(len(buffer)-1)

	# Store feature set
	for word in vocabulary:
		if word in buffer:
			out.write("1,")
		else:
			out.write("0,")
	out.write(str(value))
	out.write("\n")

out.close()
file.close()
