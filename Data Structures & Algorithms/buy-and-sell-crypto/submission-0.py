class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        sell = 0

        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            elif prices[i] - buy > sell:
                sell = prices[i] - buy
        return sell
        