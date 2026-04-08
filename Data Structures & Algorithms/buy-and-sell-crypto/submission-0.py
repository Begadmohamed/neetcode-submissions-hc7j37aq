class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        i=0
        j=1
        
        while j<len(prices) :
            if prices[i]<prices[j]:
                profit= prices[j]-prices[i]
                if profit>maxProfit:
                    maxProfit=profit
            else:
                i = j
            j += 1
        return maxProfit
            