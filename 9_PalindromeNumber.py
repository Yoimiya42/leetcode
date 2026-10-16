# 9.Palindrome Number 
    # Given an integer x, return true if x is a palindrome, and false otherwise.

class Palindrome:
    # solution 1: convert to string and compare with reversed string
    # Time complexity: O(n)
    def isPalindrome(self, x:int) ->bool:
        if x < 0:
            return False
        
        s = str(x)

        return s == "".join(reversed(s))
    
    # solution 2: convert to string and compare with reversed string by slicing
    def isPalindrome2(self, x:int) ->bool:
        if x < 0:
            return False
        s = str(x)

        return s == s[::-1]
    
    # solution 3: reverse half of the number
    # Time complexity: O(log(n))
    def isPalindrome3(self, x:int) -> bool:
        
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        rev = 0
        while(rev < x):
            rev = rev * 10 + x % 10
            x //= 10

        return rev == x or rev // 10 == x
