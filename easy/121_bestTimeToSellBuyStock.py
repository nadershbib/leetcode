class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapestBuy =  prices[0]
        maxProfit = 0 
        for price in prices:
            profit = price - cheapestBuy
            if profit > maxProfit:
                maxProfit = profit
            if price < cheapestBuy:
                cheapestBuy = price 
        return maxProfit


print(Solution().maxProfit([6,6,5,11]))

# O(n) solution
# Hope code that apparently works, August 2 2026, will trace it later, pattern recognition kicking in...

