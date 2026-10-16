# /*
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# */


class Valid:
    def isValid(self, s):
        while("()" in s or "[]" in s or "{}" in s):
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        return s == ""
    
    def isValid_stack(self, s):
        stack = []
        brackets_dict = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for c in s:
            if c in brackets_dict.keys():
                stack.append(c)
            elif not stack or brackets_dict[stack.pop()] != c:
                return False
            
        return not stack
            

if __name__ == '__main__':
    str = "{[[[(())]]]}"
    valid = Valid()
    print(valid.isValid(str))

        