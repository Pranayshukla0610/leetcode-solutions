class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            w = word.lower()

            if w[0] in row1:
                row = row1
            elif w[0] in row2:
                row = row2
            else:
                row = row3

            if all(char in row for char in w):
                result.append(word)

        return result

        