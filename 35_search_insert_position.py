"""
Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        for n in nums:
            if n == target:
                return i
            elif n > target:
                return i
            i += 1
        return i


def main():
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))
    nums = [1, 3, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))
    nums = [1, 3, 5, 6]
    target = 0
    print(Solution().searchInsert(nums, target))
    nums = [-1, -3, -5, -6]
    target = -4
    print(Solution().searchInsert(nums, target))


if __name__ == '__main__':
    main()
