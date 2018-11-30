import random
import bruteforce as bruteforce
import bottomup as bottom_up
import topdown as topdown
import test_util as test

def main():

    # Test method 1: generate random data:
    # Weights =  generateData(5, 1,10)
    # Values = generateData(5, 10, 100)
    # runTestCase();
    runExperiments();

#############################################
# EXPERIMENTS
# Generate random data.
# 1 - Same n, varried W:
def runExperiments():
    print("======> Running Experiments...")
    #Generate randome int array for weights and values
    # array's len = 10, random int from [start, end], capacity W random
    n = 20; start=10; end=100;
    Weights = test.generateData(n, start, end)
    Values = test.generateData(n, start, end)

    print("=======================================")
    print("Weights={}, Values={}".format(Weights,Values))
    # run this 100 times:
    for i in range(25):

        W = random.randint(start,end)

        print("=======================================")
        print("W={}".format(W))

        # Calling bruteforce:
        bf = bruteforce.knapsack_brute_force(Weights, Values, W);
        print("Output from brute force: ", getItemIdx(bf[0]))
        writeToFile(n, bf[1]) # recording the time it takes.

        # Calling bottom_up:
        bu = bottom_up.knapsack_bottom_up_dp(Weights, Values, W);
        print("Output from bottom up: ", getItemIdx(bu[0]))
        writeToFile(n, bu[1]) # recording the time it takes.
        print("=======================================")

        # td = topdown.knapsack_top_down_dp(Weights, Values, W);
        # print("Output from top down: ", getItemIdx(td))
        # writeToFile()



# Append or create a file:
# Save data to file,
# example: "experiments/10n_varried_W.txt" for n=10
def writeToFile(n, data):
    fileName = "experiments/"+str(n)+"n_varried_W.txt"
    f = open(fileName, "a")
    f.write(str("%.3f" % data) + "\n")

#############################################
# TEST IF OUR IMPLEMENTATIONS RETURN CORRECT RESULTS
# Using test found online(http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
# getTestData(weightsFileName, valuesFileName,resultFileName,capFileName)
# Example: test.getTestData("p01_w.txt","p01_v.txt","p01_s.txt","p01_c.txt")
# Test file has ending: weights: "_w.txt", values/profits: "_p.txt",
#                       selected items: "_s.txt", max capacity: "_c.txt"
def runTestCase():
    print("Running test case to make sure code is correct...")
    data = test.getTestData("test_case/p01_w.txt","test_case/p01_p.txt","test_case/p01_s.txt","test_case/p01_c.txt")

    Weights = data[0]
    Values = data[1]
    Results = data[2]
    W = data[3]

    print("=======================================")
    print("Weights={}, Values={}, W={}".format(Weights,Values,W))
    print("Expected result's selected item: {}".format(Results))
    print("=======================================")

    # Calling implemented functions:
    bf = bruteforce.knapsack_brute_force(Weights, Values, W);
    print("Output from brute force: ", getItemIdx(bf[0]))

    bu = bottom_up.knapsack_bottom_up_dp(Weights, Values, W);
    print("Output from bottom up: ", getItemIdx(bu[0]))

    td = topdown.knapsack_top_down_dp(Weights, Values, W);
    print("Output from top down: ", getItemIdx(td))

#################################
# Helper func:
# From the 1/0 boolean array, get the indices:
def getItemIdx(booleanArray):
    output = []
    for i in range(len(booleanArray)):
        if booleanArray[i] is 1:
            output.append(i) #get index
    return output;

#main
if __name__ == '__main__':
    main()
