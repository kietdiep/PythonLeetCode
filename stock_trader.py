#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

prices = [7,1,5,3,6,4]

def maxProfit(prices): 
    if len(prices) < 2:
        return 0
    
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] - prices[i] > 0:
            profit += prices[i+1] - prices[i]
    return profit
    

print(maxProfit(prices))
