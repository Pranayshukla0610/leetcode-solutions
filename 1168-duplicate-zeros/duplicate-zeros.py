class Solution:
    def duplicateZeros(self, arr):
        i = 0
        n = len(arr)
        
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)  # insert AFTER current zero
                arr.pop()
                i += 2   # skip both zeros
            else:
                i += 1
            
        