# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- local definitions (do not submit) ----
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---- submit below this line ----
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        pass
