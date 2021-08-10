class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        maxProfit = float('-inf')
        
        if len(prices) == 0:
            return 0
        
        minPrice = float('inf')
        maxProfit = float('-inf')
        
        for i in range(len(prices)):
            
            if prices[i] < minPrice:
            # update
                minPrice = prices[i]
            # Check for the gains
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
                
                
        return maxProfit
                    
            
            
        