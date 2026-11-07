class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for i in prices :
            if i < minBuy :
                minBuy = i
            
            if maxProfit < (i - minBuy) :
                maxProfit = i - minBuy
                
        
        return maxProfit