"""
Link - https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""

def isValid(s: str) -> bool:
    stack = []
    # lets keep all closing brackets in keys and opening brackets in values
    dict = {")": "(", "}": "{", "]": "["}
    for char in s:
        # if char is a opening bracket
        if char in dict.values():
            # append it to the stack
            stack.append(char)
        # if char is a closing bracket
        elif char in dict.keys():
            # check if the stack is empty, if yes then not valid
            # or if the value corresponding to the key(char) is not equal to the last element of the stack
            # if yes then it is not valid as per the rules/conditions above
            # In any other case it will be invalid
            if len(stack) == 0 or dict[char] != stack.pop():
                return False
        else: 
            return False
    return len(stack) == 0 

if __name__ == "__main__":
    s = input()
    print(isValid(s))
