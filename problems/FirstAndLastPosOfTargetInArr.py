# Runtime: 84 ms, faster than 68.67% of Python3 online submissions for Find First and Last Position of Element in
# Sorted Array.
# Memory Usage: 15.5 MB, less than 47.86% of Python3 online submissions for Find First and Last
# Position of Element in Sorted Array.

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = []
        output.append(self.findFirst(nums, target))
        output.append(self.findLast(nums, target))
        return output

    def findFirst(self, nums: List[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
            if nums[mid] == target:
                index = mid
        return index

    def findLast(self, nums: List[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
            if nums[mid] == target:
                index = mid
        return index