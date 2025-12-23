# 题目链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/?envType=problem-list-v2&envId=shujujiegouyusuanfa-xianxingqiantan-zhan

class Solution:
    def operator(self,s:str) -> bool:
        if s in ['-','*','/','+'] and len(s) == 1:
            return True
        return False
    def algorithm(self,s:str,left:int,right:int):
        if s == '/':return int(left / right)
        elif s == '*':return left * right
        elif s == '-':return left - right
        return left + right
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i,s in enumerate(tokens):
            if self.operator(s) == True:
                right = int(stack.pop())
                left = int(stack.pop())
                num = self.algorithm(s,left,right)
                stack.append(num)
            else:
                stack.append(int(s))
        return stack[len(stack)-1]

if __name__ == "__main__":
    print(Solution().evalRPN(["2","1","+","3","*"]))