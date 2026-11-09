# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- submit below this line ----
class Solution:
    dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    def romanToInt(self, s: str) -> int:
        value = 0

        for i in range(len(s)):
            char = s[i]
            v = self.dict[char]
            if i < len(s) - 1 and v < self.dict[s[i+1]]:
                value -= v 
            else:
                value += v
        return value
