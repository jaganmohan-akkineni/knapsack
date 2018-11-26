
import time

# BruteForce:
def Knapsack_bf(weights, values, W):
    if (len(weights)!=len(values)) or len(weights)==0 or len(values)==0 or W==0:
        print("Invalid weights array or values array or invalid length")
        return [];

    S =[]
    #set up S
    for x in range(len(weights)):
        S.append(-1);

    start = time.time() # in sec
    result = doBruteForce(weights, values,W, S);
    end = time.time()
    #result is a tuple of (selection array, totalValue, totalWeight)
    print(result)
    print("\n BruteForce: Max values={}, items={}, duration(seconds)={}".format(result[1], result[0],(end-start)*1000))

    return result[0];

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
            # adding up W and V for any 1's in S for this combination
            if(S[k] == 1):
                totalW = totalW + weights[k]
                totalV = totalV + values[k]

        # update maxV and maxW if this combo is good:
        if ((totalV > maxV) and (totalW <= W)):
            maxV = totalV;
            maxW = totalW;
            best = S.copy();

    return (best,maxV,maxW)
