
import time

# BruteForce:
def knapsack_brute_force(weights, values, W):
    if (len(weights)!=len(values)) or len(weights)==0 or len(values)==0 or W==0:
        print("Invalid weights array or values array or invalid length")
        return [];

    S =[]
    #set up S
    for x in range(len(weights)):
        S.append(-1);

    start = time.time() # in sec
    result = _doBruteForce(weights, values,W, S);
    # print("\nBruteForce: booleanArr={}".format(result))
    output = [] # get optimal set:
    for i in range(len(result)):
        if result[i] is 1:
            output.append(i) #get index

    end = time.time()
    duration = (end-start)*1000 # to milli
    return (output, duration);

# do brute force:
def _doBruteForce(weights, values,W, S):
    n = len(weights);
    maxV = maxW = 0;
    selectedItems = [] # to keep the best combination so far

    # run over 2^n posibility:
    for i in range (2**n):
        totalW = totalV = 0;

        # do all combinations of 1/0 in s:
        j = n-1;
        while(S[j] !=0 and j >= 0):
            S[j] = 0
            j = j - 1;
        S[j] = 1;

        # Start calculation weights and value, from combo in S:
        for k in range (n):
            # adding up W and V for any 1's in S for this combination
            if(S[k] == 1):
                totalW = totalW + weights[k]
                totalV = totalV + values[k]

        # if this combo is good, update maxV, maxW, and selected list :
        if ((totalV > maxV) and (totalW <= W)):
            maxV = totalV;
            maxW = totalW;
            selectedItems = S.copy();

    return selectedItems
