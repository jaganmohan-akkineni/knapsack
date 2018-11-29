import time

def knapsack_bottom_up_dp(weights, values, W):
    if (len(weights)!=len(values)) or len(weights)==0 or len(values)==0 or W==0:
        print("Invalid weights array or values array or invalid length")
        return [];
    n = len(weights)

    # create 2d array S:
    S = [[0 for x in range(W+1)] for y in range(n+1)]

    start = time.time()
    S = doBottomUp(weights,values,W,S)
    result = backtracking(S, weights)
    end = time.time()

    print("\n Bottom-up : Max values={}, items={}, duration(seconds)={}".format(S[n][W], result,(end-start)*1000))
    return result;
#####################################
# Calculating the 2d matrix S for max value
# within the capacity W
def doBottomUp(weights, values, W, S):
    #use the copy of original arrays since we dont want to make any changes to original data
    wArray = weights.copy(); vArray = values.copy()
    wArray.insert(0,0); vArray.insert(0,0); # pad a 0 in the front

    n = len(wArray);

    for i in range(n):
        for j in range(W+1):
            if j < wArray[i]:
                S[i][j] = S[i-1][j] # i not selected, fill up the cell with prev
            else:
                S[i][j] = max(S[i-1][j], S[i-1][j-wArray[i]] + vArray[i])

    return S #2d matrix with computation of optimal values

###############################
# Backtracking from optimal array S in order to get
# the index of which items including in optimal result
# S: S is list of arrays of computed values
# weights: original input weights array.
###############################
def backtracking(S, weights):
    row = len(S)-1 # number of row should be len of S
    col = len(S[0])-1 # number of column is how many items in one of array in S
    R = []

    # set up empty array R to get index of items
    for i in range (len(weights)):
        R.append(0)

    # starting from bottom right corner: S[row][col]
    while (col > 0 and row >0):
        if S[row][col] != S[row-1][col]:
            R[row-1] = 1;
            row = row-1; # move up 1 row
            col = col - weights[row] # jump to column col-weights[row]
        else:
            row=row-1 #item not selected, move to next item

    return R;
