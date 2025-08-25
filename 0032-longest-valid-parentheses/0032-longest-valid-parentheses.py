class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len=0
        stack.append(-1)
        for i,char in enumerate(s):
            if char=='(':
                stack.append(i)
            if char==')':
                p=stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len=max(max_len,i-stack[-1])
        return max_len

                