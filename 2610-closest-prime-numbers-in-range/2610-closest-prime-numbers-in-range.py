class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def find_prime(n):
            p = 2
            prime[0] = False
            prime[1] = False
            while (p * p <= n):

                # If prime[p] is not
                # changed, then it is a prime
                if (prime[p] == True):

                    # Update all multiples of p
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
            
        prime = [True for i in range(right+1)]
        find_prime(right)

        curr_diff = -1
        min_diff = float('inf')

        min_left = -1
        min_right = -1

        last_prime = 0

        for p in range(left, right+1):
            if prime[p] and last_prime:
                curr_diff = p - last_prime
                if curr_diff < min_diff:
                    min_diff = curr_diff
                    min_left = last_prime
                    min_right = p
                last_prime = p
            elif prime[p] and not last_prime:
                last_prime = p
        
        return [min_left, min_right]
                

        