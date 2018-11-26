import random
import bruteforce as bruteforce;
import bottomup as bottom_up;
import topdown as topdown


def main():
    # Weights = [4,5,9,1,2,3] #generateData(5, 1,10)
    # Values = [10,20,15,10,20,15] #generateData(5, 10, 100)

    Weights = [4,5,5] #generateData(5, 1,10)
    Values = [10,20,15] #generateData(5, 10, 100)
    W = 10

    print("Weights={}, Values={}, W={}".format(Weights,Values,W))

    # brute force:
    bf = bruteforce.Knapsack_bf(Weights, Values, W);
    td = topdown.Knapsack_topdown(Weights, Values, W);
    bu = bottom_up.Knapsack_bottomup(Weights, Values, W);

################################
# n : array lengths that will be generatedself.
# start, end: random number's range
# generating arrays of weights and values of random int of length n:
def generateData(n, start, end):
    print("Generating data of length: {}, start={}, end={} ".format(n,start,end))
    arr = [];
    for x in range(n):
        arr.append(random.randint(start,end))

    return arr




if __name__ == '__main__':
    main()
