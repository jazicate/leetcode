# 122. Best Time to Buy and Sell Stock II - medium
class Solution:
    def maxProfit(self, prices: List[int]) -> int: # O(n) time, O(1) space
        '''
            Same thing as the first version, but the idea is to just increment profit if there's profit -> greedy
        '''
        if len(prices) == 0: return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit