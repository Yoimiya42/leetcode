# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math

# ---- submit below this line ----
class Solution:
    # def transpose(self, matrix: list[list[int]], r:int, c:int) -> None:

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            k, j = 0, len(matrix[0]) - 1
            while k < j:
                matrix[i][k], matrix[i][j] = matrix[i][j], matrix[i][k]
                k+=1
                j-=1