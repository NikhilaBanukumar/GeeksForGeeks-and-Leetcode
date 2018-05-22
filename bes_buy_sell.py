def maxProfit(prices):
    i = 0
    j = 1
    cost = 0
    while i < j and j < len(prices):
        if prices[i] > prices[j]:
            i += 1
            j += 1
        else:
            if prices[j - 1] > prices[j]:
                cost += prices[j - 1] - prices[i]
                i = j-1
            else:
                j+=1
    if j==len(prices) and prices[j-1]>prices[i]:
        cost+=prices[j-1]-prices[i]
    print( cost)

maxProfit([6,1,3,2,4,7])