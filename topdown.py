import time

def knapsack_top_down_dp(weights, values, W):
    #print("===> Doing knapsack top down method....")

    n = len(weights)
    
    #table for backtracking and calculating maxvalue
    dptable =[[0 for x in range(n+1)] for y in range(W+1)] 
    
    start = time.time()
    x = topdown_dp_util(weights, values, W, n, 0, dptable)
    optimalset = bactracking(weights, values, dptable,n)
    end = time.time()
    durationSeconds = (end-start)*1000

    for i in range(len(dptable)):
        print(dptable[i])

    #print(optimalset)
    return optimalset, durationSeconds


def topdown_dp_util(weights, values, remainingWeight, n, currentItem, dptable):
    remainingItems = n - currentItem
    maxvalue = 0

    #if all items in the set are traversed or knapsack is full
    if(currentItem >= n or remainingWeight <= 0):
        return 0

    #if the value is already calculated.
    if(dptable[remainingWeight][remainingItems] != 0 ):
        return dptable[remainingWeight][remainingItems]

    #if the weight of currentitem is more than remaining weight, we go to next item.
    if(remainingWeight < weights[currentItem]):
        maxvalue = topdown_dp_util(weights, values, remainingWeight, n, currentItem + 1, dptable)
    else:
        #checking if picking currentitem is optimal or not.
        maxvalue = max(values[currentItem] + topdown_dp_util(weights, values, remainingWeight - weights[currentItem], n, currentItem + 1, dptable),
                        topdown_dp_util(weights, values, remainingWeight, n, currentItem + 1, dptable))
    dptable[remainingWeight][remainingItems] = maxvalue

    return maxvalue

def bactracking(weights, values, dptable,n):
    i=len(dptable)-1
    j=n
    print(i)
    print(j)
    optimalset = []

    while(i>0 and j>0):
        #if currentitem is not included in the optimal set.
        if(dptable[i][j] == dptable[i][j-1]):
            j = j-1
        #if currentitem is included in the optimal set.
        else:
            optimalset.append(n-j)

            i = i-weights[n-j]
            j = j - 1
    '''
    sum = 0
    for k in range(len(optimalset)):
        sum = sum + values[optimalset[k]]
    print('sum', sum)'''
    return optimalset

if __name__ == '__main__':

    #weights = [23,31,29,44,53,38,63,85,89,82]
    #values = [92,57,49,68,60,43,67,84,87,72]
    weights = [2, 2, 4, 5]
    values = [2, 4, 6, 9]
    W = 8

    print('answer:', knapsack_top_down_dp(weights, values, W))

