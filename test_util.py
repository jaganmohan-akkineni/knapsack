import random


################################
# read files for: weight, value, result, capcity:
# return tuples: (weights array, value array, selected item array, max capacity value)
################################
def getTestData(weightsFileName, valuesFileName,resultFileName,capFileName):
    print("Get test data from: ", weightsFileName, valuesFileName,resultFileName,capFileName)
    wList = readDataAsList(weightsFileName)
    vList = readDataAsList(valuesFileName)
    rList = readDataAsList(resultFileName)
    W = readDataAsList(capFileName)
    return(wList, vList, rList, W[0])







################################
# n : array lengths that will be generatedself.
# start, end: random number's range
# Generate Arrays of random int w/ length n:
def generateData(n, start, end):
    # print("Generating data of length: {}, random int from: [{},{}] ".format(n,start,end))
    arr = [];
    for x in range(n):
        arr.append(random.randint(start,end))

    return arr



################################
# read from a file to array of int
################################
def readDataAsList(filename):
    x = []
    list = []
    #read each line as item in a list:
    with open(filename, 'r') as f:
        x = f.readlines()

    for i in x:
        # each line: make sure to strip new line, and space
        num = i.rstrip('\n').lstrip(" ")
        list.append(int(num) )#convert to int.
    return list # array of int
