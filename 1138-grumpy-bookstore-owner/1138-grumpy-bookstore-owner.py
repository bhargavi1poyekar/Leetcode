class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        output = 0

        for i in range(n):
            output += (1 - grumpy[i]) * customers[i]
            customers[i] = grumpy[i] * customers[i]

        w_sum = max_sum = sum(customers[:minutes])

        for w_end in range(minutes, n):
            w_sum += customers[w_end] - customers[w_end - minutes]
            max_sum = max(max_sum, w_sum)

        return output + max_sum