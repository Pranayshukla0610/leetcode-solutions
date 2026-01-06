import math

class Solution:
    def maxLength(self, nums):
        max_len=0
        n = len(nums)

        for i in range(n):
            prod = 1
            gcd = 0
            lcm = 1

            for j in range(i,n):
                num = nums[j]
                gcd = math.gcd(gcd,num)
                lcm = abs(lcm*num)//math.gcd(lcm,num)
                prod *= num

                if prod == gcd*lcm:
                    max_len = max(max_len,j-i+1)
        return max_len
        