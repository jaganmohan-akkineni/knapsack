
import random;

def main():
    print("Hello, world!")
    Weights = [4,5,9,1,2,3]
    Values = [10,20,15,10,20,15]
    W = 10


    knapsack_bf(Weights, Values, W);

# BruteForce:
def knapsack_bf(weights, values, W):
    if len(weights) != len(values):
        return [];
    S =[]
    #set up S
    for x in range(len(weights)):
        S.append(-1);

    print("====> main caller knapsack_b: S={} Weights={}, Values={}".format(S,weights,values))

    result = doBruteForce(weights, values,W, S);
    #result is a tuple of (selection array, totalValue, totalWeight)
    print("result: ", result)

    #TODO: extract the selection array to return items



# do brute force:
def doBruteForce(weights, values,W, S):
    n = len(weights);
    maxV = maxW = 0;
    prevChoice = []
    # run over 2^n possibilities:
    for i in range (2**n):
        totalW = 0;
        totalV = 0;
        j = n-1;

        # this loop do all combination of 1/0 in s:
        while(S[j] !=0 and j >= 0):
            S[j] = 0
            j = j - 1;

        S[j] = 1;

        # Start calculation weights and value, look into S:
        for k in range (n):
            # adding up W and V for any 1's in S:
            if(S[k] == 1):
                totalW = totalW + weights[k]
                totalV = totalV + values[k]

        # update maxV and maxW if this combo is good:
        if ((totalV > maxV) and (totalW <= W)):
            maxV = totalV;
            maxW = totalW;
            best = S.copy();

    return (best,maxV,maxW)



if __name__ == '__main__':
    main()
