# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
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
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        pass


    def next(self) -> int:
        pass


    def hasNext(self) -> bool:
        pass



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
