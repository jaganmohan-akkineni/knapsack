def knapsack_top_down_dp(weights, values, W):
    print("===> Doing knapsack top down method....")

    n = len(weights)
    dptable =[[0 for x in range(n+1)] for y in range(W+1)]
    x = topdown_dp_util(weights, values, W, n, 0, dptable)

    optimalset = bactracking(weights, values, dptable,n)
    print(optimalset)
    return optimalset


def topdown_dp_util(weights, values, remainingWeight, n, currentItem, dptable):
    remainingItems = n - currentItem
    maxvalue = 0

    if(currentItem >= n or remainingWeight <= 0):
        return 0

    if(dptable[remainingWeight][remainingItems] != 0 ):
        return dptable[remainingWeight][remainingItems]

    if(remainingWeight < weights[currentItem]):
        maxvalue = topdown_dp_util(weights, values, remainingWeight, n, currentItem + 1, dptable)
    else:
        maxvalue = max(values[currentItem] + topdown_dp_util(weights, values, remainingWeight - weights[currentItem], n, currentItem + 1, dptable),
                        topdown_dp_util(weights, values, remainingWeight, n, currentItem + 1, dptable))
    dptable[remainingWeight][remainingItems] = maxvalue

    return maxvalue

def bactracking(weights, values, dptable,n):
    i=len(dptable)-1
    j=n
    optimalset = []

    while(i>0 and j>0):
        if(dptable[i][j] == dptable[i][j-1]):
            j = j-1
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
'''
if __name__ == '__main__':

    weights = [23,31,29,44,53,38,63,85,89,82]
    values = [92,57,49,68,60,43,67,84,87,72]
    #weights = [2, 2, 4, 5]
    #values = [2, 4, 6, 9]
    W = 165

    print('answer:', knapsack_topdown_dp(weights, values, W))
'''
