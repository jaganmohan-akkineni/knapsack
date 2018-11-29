import random
import bruteforce as bruteforce;
import bottomup as bottom_up;
import topdown as topdown
import test as test

def main():

    # Test method 1: generate random data:
    # Weights =  generateData(5, 1,10)
    # Values = generateData(5, 10, 100)

    # Test method 2: using test case found online(http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
    # getTestData(weightsFileName, valuesFileName,resultFileName,capFileName)
    # Example: test.getTestData("p01_w.txt","p01_v.txt","p01_s.txt","p01_c.txt")
    # Test file has ending: weights: "_w.txt", values/profits: "_p.txt",
    #                       selected items: "_s.txt", max capacity: "_c.txt"

    data = test.getTestData("test_case/p01_w.txt","test_case/p01_p.txt","test_case/p01_s.txt","test_case/p01_c.txt")
    Weights = data[0]
    Values = data[1]
    Results = data[2]
    W = data[3] #

    print("=======================================")
    print("Weights={}, Values={}, W={}".format(Weights,Values,W))
    print("Expected result's selected item: {}".format(Results))
    print("=======================================")

    # Calling implemented functions:
    bf = bruteforce.knapsack_brute_force(Weights, Values, W);
    bu = bottom_up.knapsack_bottom_up_dp(Weights, Values, W);
    td = topdown.knapsack_top_down_dp(Weights, Values, W);


#main
if __name__ == '__main__':
    main()
