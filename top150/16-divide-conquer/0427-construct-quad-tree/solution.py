# 427. Construct Quad Tree
# https://leetcode.com/problems/construct-quad-tree/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- local definitions (do not submit) ----
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# ---- submit below this line ----
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        pass
