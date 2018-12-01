
import bruteforce as bruteforce
import bottomup as bottom_up
import topdown as topdown
import utils as utils


def main():
    runTestCase()



#############################################
# SIMPLE TEST IF OUR IMPLEMENTATIONS RETURN CORRECT RESULTS
# Using test found online(http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
# getTestData(weightsFileName, valuesFileName,resultFileName,capFileName)
# Example: test.getTestData("p01_w.txt","p01_v.txt","p01_s.txt","p01_c.txt")
# Test file has ending: weights: "_w.txt", values/profits: "_p.txt",
#                       selected items: "_s.txt", max capacity: "_c.txt"
def runTestCase():
    print("Running test case to make sure code is correct...")
    for i in range (1,9):
        j = str(i)
        data = _getTestData("test_case/p0"+j+"_w.txt","test_case/p0"+j+"_p.txt","test_case/p0"+j+"_s.txt","test_case/p0"+j+"_c.txt")

        Weights = data[0]
        Values = data[1]
        Results = data[2]
        W = data[3]
        Expected = _getOptSet(Results)

        print("=======================================")
        print("Weights={}, Values={}, W={}".format(Weights,Values,W))
        print("Expected result's selected item: {}".format(Expected))
        print("=======================================")

        # Calling implemented functions:
        bf = bruteforce.knapsack_brute_force(Weights, Values, W);
        bu = bottom_up.knapsack_bottom_up_dp(Weights, Values, W);
        td = topdown.knapsack_top_down_dp(Weights, Values, W);

        if _isPassed(bf[0], Expected) is False:
            print("Result: {}, expected: {}".format(bf[0], Expected))
            raise ValueError('BruteForce failed at test #' + j)
        if _isPassed(bu[0], Expected) is False:
            raise ValueError('BottomUp failed at test #' + j)
            print("Result: {}, expected: {}".format(bu[0], Expected))
        if _isPassed(td[0], Expected) is False:
            print("Result: {}, expected: {}".format(td[0], Expected))
            raise ValueError('TopDown failed at test #' + j)


# from boolean arr, get optimal item indices
def _getOptSet(boolArr):
    expected = []
    for r in range(len(boolArr)): # get optimal set:
        if boolArr[r] is 1:
            expected.append(r)
    return expected;



def _isPassed(result, expected):
    if result == expected:
        return True
    else:
        return False
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
