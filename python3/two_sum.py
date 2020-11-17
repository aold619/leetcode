#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

from typing import List


# @lc code=start
class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # @lc code=end
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #
        # return []

        n = len(nums)
        hash_table = dict()
        for i in range(n):
            x = hash_table.get(target - nums[i])
            if x is not None:
                return [x, i]
            hash_table[nums[i]] = i

        return []
