# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- submit below this line ----
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        count = {}
        for c in magazine:
            count[c] = count.get(c, 0) + 1

        for c in ransomNote:
            if count.get(c) is None or count.get(c) <= 0:
                return False
            count[c] -=1
            
        return True
        
