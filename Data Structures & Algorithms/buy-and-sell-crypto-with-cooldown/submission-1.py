class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)

        def processDay(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = processDay(i + 1, buying)
            secondOption = None
            if buying:
                secondOption = processDay(i + 1, not buying) - prices[i]
            else:
                secondOption = processDay(i + 2, not buying) + prices[i]
            dp[(i, buying)] = max(cooldown, secondOption)

            return dp[(i, buying)]

        return processDay(0, True)