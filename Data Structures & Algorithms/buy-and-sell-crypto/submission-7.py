class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMaxProfit = 0
        leftPtr = 0
        rightPtr = 0

        while rightPtr < len(prices):
            if prices[leftPtr] < prices[rightPtr]:
                profit = prices[rightPtr] - prices[leftPtr]
                currMaxProfit = max(currMaxProfit, profit)
            else:
                leftPtr = rightPtr
            rightPtr += 1
        return currMaxProfit

        