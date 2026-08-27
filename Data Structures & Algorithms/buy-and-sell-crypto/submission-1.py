class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDate = 0
        sellDate = 1
        maxProfit = 0
        while sellDate < len(prices):
            maxProfit = max(maxProfit, prices[sellDate] - prices[buyDate])
            if prices[sellDate] < prices[buyDate]: buyDate = sellDate
            sellDate += 1

        return maxProfit
            
