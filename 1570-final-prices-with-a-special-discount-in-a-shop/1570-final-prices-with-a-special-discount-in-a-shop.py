class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        mono_stack = []
        discount = prices

        for i in range(len(prices)):
            while mono_stack and prices[mono_stack[-1]] >= prices[i]:
                index = mono_stack.pop()
                discount[index] = prices[index] - prices[i]
            mono_stack.append(i)
        return discount   