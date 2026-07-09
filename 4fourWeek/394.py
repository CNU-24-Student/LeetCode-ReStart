from typing import List
import json

VALUES = "qwertyuiopasdfghjklzxcvbnm"

def function(s:str) -> str:
    n = len(s)
    ans = ""
    num = 0
    i = 0
    stack = []
    while i < n:
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == '[':
            stack.append((ans,num))
            ans = ""
            num = 0
        elif s[i] == ']':
            last_ans,last_num = stack.pop()
            ans = last_ans + ans * last_num
        else:
            ans += s[i]
        i += 1
        
    return ans

if __name__ == "__main__":
    s = input()
    print(function(s))