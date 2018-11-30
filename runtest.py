
import bruteforce as bruteforce
import bottomup as bottom_up
import topdown as topdown
import utils as utils


def main():
    runTestCase()



#############################################
# TEST IF OUR IMPLEMENTATIONS RETURN CORRECT RESULTS
# Using test found online(http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
# getTestData(weightsFileName, valuesFileName,resultFileName,capFileName)
# Example: test.getTestData("p01_w.txt","p01_v.txt","p01_s.txt","p01_c.txt")
# Test file has ending: weights: "_w.txt", values/profits: "_p.txt",
#                       selected items: "_s.txt", max capacity: "_c.txt"
def runTestCase():
    print("Running test case to make sure code is correct...")
    data = _getTestData("test_case/p01_w.txt","test_case/p01_p.txt","test_case/p01_s.txt","test_case/p01_c.txt")

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
    bu = bottom_up.knapsack_bottom_up_dp(Weights, Values, W);
    td = topdown.knapsack_top_down_dp(Weights, Values, W);


################################
# read files for: weight, value, result, capcity:
# return tuples: (weights array, value array, selected item array, max capacity value)
################################
def _getTestData(weightsFileName, valuesFileName,resultFileName,capFileName):
    print("Get test data from: ", weightsFileName, valuesFileName,resultFileName,capFileName)
    wList = utils.readDataAsList(weightsFileName)
    vList = utils.readDataAsList(valuesFileName)
    rList = utils.readDataAsList(resultFileName)
    W = utils.readDataAsList(capFileName)
    return(wList, vList, rList, W[0])



#main
if __name__ == '__main__':
    main()
