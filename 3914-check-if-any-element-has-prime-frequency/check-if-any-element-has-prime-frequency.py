from collections import Counter
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2,int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        for count in freq.values():
            if is_prime(count):
                return True
        return False
        