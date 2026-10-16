# 289. Game of Life
# https://leetcode.com/problems/game-of-life/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- submit below this line ----
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
