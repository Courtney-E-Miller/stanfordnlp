
# Reads in original training data from paper
originalBinaryTreeData = open("Labeled SO for CoreNLP.txt", 'r')
num0 = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
numrows = 0
for line in originalBinaryTreeData:
    numrows += 1
    if line[1] == '0':
        num0 += 1
        print("this is a very positive (0)", line)
    if line[1] == '1':
        num1+=1
    elif line[1] == '2':
        num2 += 1
    elif line[1] == '3':
        #print("this is a negative (3)", line)
        num3 += 1
    elif line[1] == '4':
        num4 += 1
        print("this is a very negative (4) ", line)

print("total number of rows", numrows)
print("num of 0s", num0)
print("num of 1s", num1)
print("num of 2s", num2)
print("num of 3s", num3)
print("num of 4s", num4)


