def Knapsack_topdown_dp(weights, values, W):
    print("===> Doing knapsack top down method....")
    n = len(weights)
    #dptable =[[0]*(n+1)]*(W+1)
    dptable =[[0 for x in range(n+1)] for y in range(W+1)]
    x = topdown_dp_util(weights, values, W, n, 0, dptable)
    #print(dptable)
    #for i in range(len(dptable)):
     #   print(dptable[i])
    i=W
    j=n
    print(dptable[W][n])
    print(weights[n-j])
    print(dptable[i-weights[n-j]][j-1])
    while(i>0 and j>0):
        print(dptable[i-weights[n-j]][j-1])

        if(dptable[i][j] == dptable[j-weights[n-j]][i-1] + weights[n-j]):
            print(n-j)
            j = j - 1
            i = i-weights[n-i]
        else:
            j = j-1
    return x


def topdown_dp_util(weights, values, remainingWeight, n, currentItem, dptable):
    
    if(currentItem >= n or remainingWeight <= 0):
        return 0

    remainingItems = n - currentItem
    if(dptable[remainingWeight][remainingItems] != 0 ):
        print('found dp(', remainingWeight, remainingItems, ') = ', dptable[remainingWeight][remainingItems])
        return dptable[remainingWeight][remainingItems]

    maxvalue = 0

    if(remainingWeight < weights[currentItem]):
        maxvalue = topdown_dp_util(weights, values, remainingWeight, n, currentItem + 1, dptable)
    else:
        maxvalue = max(values[currentItem] + topdown_dp_util(weights, values, remainingWeight - weights[currentItem], n, currentItem + 1, dptable),
                        topdown_dp_util(weights, values, remainingWeight, n, currentItem + 1, dptable))
    dptable[remainingWeight][remainingItems] = maxvalue

    return maxvalue

if __name__ == '__main__':
    
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82, ]
    values = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    W = 165

    print('answer:', Knapsack_topdown_dp(weights, values, W))
