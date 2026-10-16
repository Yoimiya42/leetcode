# 125. Valid Palindrome
    # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    # Given a string s, return true if it is a palindrome, or false otherwise.
from typing import List
 
class VP:
    # solution 1 : rebuild the string and compare with its reversed
    # Time complexity: O(n)
    def isValidPalindrome(self, s:str) -> bool:
        newStr : List[str] = []
        for ch in s:
            if ch.isalnum():
                newStr.append(ch.lower())

        return newStr == newStr[::-1]
    
    # solution 2: two pointers
    # Time complexity: O(n)
    def isValidPalindrome2(self, s:str) -> bool:

        newStr : List[str] = []
        for ch in s :
            if ch.isalnum():
                newStr.append(ch.lower())

        front = 0
        rear = len(newStr) - 1
        while(front < rear):
            if newStr[front] != newStr[rear]:
                return False
            front += 1
            rear  -= 1

        return True
    




