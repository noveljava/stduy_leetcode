from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit = 0
        hold = None

        for day in range(len(prices)-1):
            if hold is None:
                hold = prices[day]

            if prices[day] > prices[day+1]:
                benefit += prices[day] - hold
                hold = None

        if hold is not None:
            benefit += prices[-1] - hold

        return benefit

# prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))