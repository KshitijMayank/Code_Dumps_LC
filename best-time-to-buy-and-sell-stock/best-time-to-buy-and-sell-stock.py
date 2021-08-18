class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Get the min price and then sell it at max profit
        
        minPrice = float('inf')
        maxProfit = float('-inf')
        if len(prices) == 1 | len(prices) == 0:
            return 0
        for i in prices:
            
            if i < minPrice:
                minPrice = i
            if i - minPrice > maxProfit:
                maxProfit = i - minPrice
        return maxProfit
        
        