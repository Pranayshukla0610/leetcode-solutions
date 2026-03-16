from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_set = set(friends)
        result = []

        for x in order:
            if x in friend_set:
                result.append(x)

        return result


        