class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_price = prices[0] + fee
        # Initialize the maximum profit as 0
        max_profit = 0
        
        # Iterate over each stock price
        for price in prices:
            # If the current price is greater than the minimum price,
            # a profit can be made by selling the stock
            if min_price < price:
                # Add the difference between the current price and the minimum price
                # to the maximum profit
                max_profit += price - min_price
                # Update the minimum price to the current price
                min_price = price
            # If the current price plus fee is less than the minimum price,
            # update the minimum price to the current price plus fee
            elif price + fee < min_price:
                min_price = price + fee
        
        # Return the maximum profit
        return max_profit