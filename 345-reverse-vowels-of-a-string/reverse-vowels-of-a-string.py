class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vow = 'aeiouAEIOU'
        l, r = 0, len(s) - 1
        while l < r:
            if l < r and s[l] not in vow:
                l += 1
            elif l < r and s[r] not in vow:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
        