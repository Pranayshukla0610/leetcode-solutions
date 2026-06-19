class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            l = 0
            r = len(i)-1
            while l < r:
                if i[l] != i[r]:
                    break
                l +=1
                r -=1
            if l >= r:
                return i
        return ""
        