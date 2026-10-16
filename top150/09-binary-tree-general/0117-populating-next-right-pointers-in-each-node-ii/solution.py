# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- local definitions (do not submit) ----
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# ---- submit below this line ----
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pass
