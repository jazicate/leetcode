# 121. Best Time to Buy and Sell Stock - easy
class Solution:
    def maxProfit(self, prices: List[int]) -> int: # O(n) time, O(1) space
        ''' 
            Find the best profit in the whole list (choose the best day to buy a stock and a different day to sell that stock)


            Edge case: if prices is empty -> just return 0

            Keep track of a global lowest stock
            Keep track of the a global max profit

            Loop through prices:
            - Check if stock is lower than the lowest_stock found so far -> if it is, then replace the lowest_stock with the current stock
            - Else, continue finding the profit with the current lowest stock
              - if the profit from this stock is higher -> replace profit with that profit
        '''

        if not prices:
            return 0

        lowest_stock = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < lowest_stock:
                lowest_stock = prices[i]
            else:
                candidate_profit = prices[i] - lowest_stock

                if (candidate_profit > profit):
                    profit = candidate_profit
        
        return profit

