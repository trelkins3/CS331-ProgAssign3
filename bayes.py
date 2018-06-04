import numpy as np
import string

train = open('trainingSet.txt')
test  = open('testSet.txt')
out  = open("preprocessed_train.txt","w")
testout = open("preprocessed_test.txt","w")

##### Train Section #####
vocabulary = []

for line in train:
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

features  = []
positives = []
negatives = []
values 	 = []
i = 0
poscount = 0
negcount = 0

#	Generate Feature Set
train.seek(0)
for line in train:
	# Tokenize the line
	buffer = line.split()
	features.append([])

	# Store the classlable and remove it from buffer
	values.append(buffer[len(buffer)-1])
	buffer.pop(len(buffer)-1)
	
	if(int(values[i]) == 1):
		positives.append([])
	else:
		negatives.append([])

	k = 0
	for object in buffer:
		# Strip punctuation and make lower case
		buffer[k] = (object.translate(None, string.punctuation)).lower()
		k += 1

	# Store feature set
	for word in vocabulary:
		# If the review is positive store it in the positives
		if(int(values[i]) == 1):
			if word in buffer:
				positives[poscount].append(1)
				features[i].append(1)
				out.write("1,")
			else:
				positives[poscount].append(0)
				features[i].append(0)
				out.write("0,")
		# If the review is negative store it in the negatives
		else:
			if word in buffer:
				negatives[negcount].append(1)
				features[i].append(1)
				out.write("1,")
			else:
				negatives[negcount].append(0)
				features[i].append(0)
				out.write("0,")
		
	if(int(values[i])==1):
		poscount += 1
	else:
		negcount += 1
	features[i].append(int(values[i]))
	out.write(str(values[i]))
	out.write("\n")
	i += 1

total = i	
# Percentage of positive reviews
poschance = float(poscount) / float(total)
negchance = float(negcount) / float(total) 
print("poscount: ", poscount)
print("negcount: ", negcount)
print("total: ", total)
print("label percentage: ", poschance)
print("Not label percentage: ", negchance)

# Sums of positive and negative feature sets
possums = []
for i in range(0,len(vocabulary)-1):
	possums.append(0)
	for j in range(0, poscount-1):
		possums[i] = (int(possums[i]) + positives[j][i])
negsums = []
for i in range(0,len(vocabulary)-1):
	negsums.append(0)
	for j in range(0, negcount-1):
		negsums[i] = (int(negsums[i]) + negatives[j][i])

# Probabilities of positives and negatives features sets
posprob1 = []
posprob0 = []
for i in range(0,len(possums)):
	posprob1.append(0)
	posprob0.append(0)
	posprob1[i] = (float(possums[i])+1)/(float(poscount)+2)
	posprob0[i] = (float(poscount)-float(possums[i])+1)/(float(poscount)+2)
negprob1 = []
negprob0 = []
for i in range(0,len(negsums)):
	negprob1.append(0)
	negprob0.append(0)
	negprob1[i] = (float(negsums[i])+1)/(float(negcount)+2)
	negprob0[i] = (float(negcount)-float(negsums[i])+1)/(float(negcount)+2)

# Predict training data
train.seek(0)
results  = []
i = 0
for line in train:
	postemp1 = 1
	postemp0 = 1
	negtemp1 = 1
	negtemp0 = 1
	postemp  = 1
	negtemp  = 1
	# Tokenize  the line
	buffer = line.split()

	# Remove the classlabel
	buffer.pop(len(buffer)-1)

	# Strip punctuation and make lower case
	k = 0
	for object in buffer:
		buffer[k] = (object.translate(None, string.punctuation)).lower()
		k += 1
	
	for j in range(0,len(vocabulary)-1):
		if vocabulary[j] in buffer:
			postemp1 = float(postemp1)*float(posprob1[j])
			negtemp1 = float(negtemp1)*float(negprob1[j])
		else:
			postemp0 = float(postemp0)*float(posprob0[j])
			negtemp0 = float(negtemp0)*float(negprob0[j])

	postemp = float(postemp1)*float(postemp0)*float(poschance)
	negtemp = float(negtemp1)*float(negtemp0)*float(negchance)

	results.append(0)
	if (float(postemp)>float(negtemp)):
		results[i] = 1
	else:
		results[i] = 0

	i += 1

print("results: ",results)
print("length: " ,len(results))

correct = 0
for i in range(0,total):
	if (int(results[i]) == int(values[i])):
		correct += 1

accuracy = float(correct)/float(total)
print("accuracy: ", accuracy)



##### Test section #####
testvocab = []

for line in test:
	# Tokenize the line
	buffer = line.split()

	# Remove the classlabel
	buffer.pop(len(buffer)-1)
	
	for object in buffer:
		# Strip punctuation and make lower case
		object = (object.translate(None, string.punctuation)).lower()
		if object not in testvocab:
			testvocab.append(object)

# Alphabetize
testvocab.sort()

# Write vocab to file
for word in testvocab:
	testout.write(str(word))
	testout.write(",")

testout.write("classlabel\n")

testfeatures = []
testvalues   = []
i = 0
testHold = 0

#	Generate Feature Set
test.seek(0)
for line in test:
	testfeatures.append([])
	# Tokenize the line
	buffer = line.split()

	# Store the classlable and remove it from buffer
	testvalues.append(buffer[len(buffer)-1])
	buffer.pop(len(buffer)-1)

	k = 0
	for object in buffer:
		# Strip punctuation and make lower case
		buffer[k] = (object.translate(None, string.punctuation)).lower()
		k += 1

	# Store feature set
	j = 0
	for word in testvocab:
		if word in buffer:
			testfeatures[i].append(1)
			testout.write("1,")
		else:
			testfeatures[i].append(0)
			testout.write("0,")
		j += 1
	
	testfeatures[i].append(int(testvalues[i]))
	testout.write(str(testvalues[i]))
	testout.write("\n")
	i += 1

print(len(testfeatures[0]))
print(len(testvocab))
print(len(features[0]))
print(len(vocabulary))
out.close()
testout.close()
train.close()

# Let's compartmentalize some of these into functions so it's easier to read
