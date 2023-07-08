class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack=[]

        final_price=prices

        for p in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[p]:
                index=stack.pop()
                final_price[index]=prices[index]-prices[p]
            
            stack.append(p)
        
        return(final_price)