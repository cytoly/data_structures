# Runtime: 348 ms, faster than 71.78% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 21.6 MB, less than 83.80% of Python3 online submissions for Find All Duplicates in an Array.

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        found = []
        for i in nums:
            val = nums[abs(i) - 1]
            if val > 0:
                nums[abs(i) - 1] = -val
            else:
                found.append(abs(i))
        return found