class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        maxProfit = float('-inf')
        minPrice = prices[0]
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            maxProfit = max(maxProfit, price - minPrice)
        
        return maxProfit