# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- local definitions (do not submit) ----
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ---- submit below this line ----
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        pass
