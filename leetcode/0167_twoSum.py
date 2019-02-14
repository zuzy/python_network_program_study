#!/usr/bin/python3

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(numbers):
            t = target - n
            for j, m in enumerate(numbers[::-1]):
                if m > t:
                    continue
                elif m < t:
                    break
                else:
                    return [i, j]