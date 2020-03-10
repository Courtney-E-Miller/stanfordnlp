import random
import csv

# Reads in original training data from paper
originalBinaryTreeData = open("Labeled SO for CoreNLP.txt", 'r')

originalPos = []
originalNeu = []
originalNeg = []

for line in originalBinaryTreeData:
    if line[1] == '0':
        originalNeg.append(line)
    if line[1] == '1':
        originalNeg.append(line)
    elif line[1] == '2':
        originalNeu.append(line)
    elif line[1] == '3':
        originalPos.append(line)
    elif line[1] == '4':
        originalPos.append(line)

# Creating upsampled positive componet
upsampledPosComponet = random.choices(originalPos, k=(len(originalNeu) - len(originalPos)))

# Creating upsampled negative componet
upsampledNegComponet = random.choices(originalNeg, k=(len(originalNeu) - len(originalNeg)))

upsampledBinaryTreeData = originalPos + upsampledPosComponet + originalNeu + originalNeg + upsampledNegComponet

# Can be used to check the distribution of a dataset as a sanity check
def checkBalance(dataset):
    numPos = 0
    numNeu = 0
    numNeg = 0

    for line in upsampledBinaryTreeData:
        if line[1] == '0':
            numPos += 1
        if line[1] == '1':
            numPos += 1
        elif line[1] == '2':
            numNeu += 1
        elif line[1] == '3':
            numNeg += 1
        elif line[1] == '4':
            numNeg += 1

    print("num pos", numPos)
    print("num neg", numNeg)
    print("num neu", numNeu)

print(upsampledBinaryTreeData)

with open("upsampledSOData.txt", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in upsampledBinaryTreeData:
        newVal = val[0:-1]
        writer.writerow([newVal])