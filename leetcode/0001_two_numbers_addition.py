#!/usr/bin/python3
#coding: utf-8

class Solution:
    def _twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums) - 1
        i = 0
        while True:
            t = target - nums[i]
            for j in range(0, length):
                if j == i:
                    continue
                if t == nums[j]:
                    return [i, j]
            i += 1
            
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            t = target - n
            for j, m in enumerate(nums[i + 1:]):
                if t == n:
                    return [n, m]
        return [-1, -1]
            