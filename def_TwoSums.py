# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 00:54:42 2024

@author: kraus
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

        return None


nums = [2, 4, 5, 7, 8, 11]
target = 10
sol = Solution()
result = sol.twoSum(nums, target)
print(result)

