class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini, maxi = 0, 1

        result = 0
        while maxi < len(prices):

            if prices[mini] < prices[maxi]:
                result = max(result, prices[maxi]-prices[mini])
            else:
                mini = maxi

            maxi += 1

        return result


# Time complexity : o(n)
# Space complexity : o(1)
