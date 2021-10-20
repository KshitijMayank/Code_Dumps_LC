class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Get the min price and then sell it at max profit
        
        min_price = float('inf')
        max_profit = float('-inf')
        
        for p in prices:
            if p < min_price:
                min_price = p
            
            cur_profit = p - min_price
            
            if cur_profit > max_profit:
                max_profit = cur_profit
            
        return max_profit
        