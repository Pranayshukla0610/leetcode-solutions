from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: count required letters from licensePlate
        required = Counter(
            ch.lower() for ch in licensePlate if ch.isalpha()
        )
        
        answer = None
        
        # Step 2: check each word
        for word in words:
            word_count = Counter(word)
            
            # Check if word satisfies all required letters
            if all(word_count[c] >= required[c] for c in required):
                if answer is None or len(word) < len(answer):
                    answer = word
        
        return answer

        