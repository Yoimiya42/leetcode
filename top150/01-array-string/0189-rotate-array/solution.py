# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- submit below this line ----
class Solution:
    def swap(self, nums:list[int], i:int, j:int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k_ = k % len(nums)
        self.swap(nums, 0, len(nums) - 1)
        self.swap(nums, 0, k_ - 1)
        self.swap(nums, k_, len(nums) - 1)

            