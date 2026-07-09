from typing import List
import json
# from collections import stack

def function(s:str) -> bool:
    stack = []
    for i in s:
        if i == '(' or i == "[" or i == '{':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif i == ')' and stack[-1] != '(':
                return False
            elif i == '}' and stack[-1] != '{':
                return False
            elif i == ']' and stack[-1] != '[':
                return False
            stack.pop()
    if len(stack)>0:return False
    return True
            
if __name__ == "__main__":
    s = input()
    print(function(s))