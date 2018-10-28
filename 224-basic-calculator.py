# 224. Basic Calculator

class Solution:
    def calculate(self,s):
        """
        :type s: str
        :rtype: int
        """
        tokens = tokenizeWithParens(s)
        # print(tokens)
        stack = []
        for t in tokens:
            if t.isdigit():
                stack.append(int(t))
            elif t in '(+-':
                stack.append(t)
            elif t == ')':
                # print(stack)
                subStack = []
                while stack[-1] != '(':
                    num = stack.pop()
                    op = stack.pop()
                    if op == '+':
                        subStack.append(num)
                    elif op == '-':
                        subStack.append(-1 * num)
                    elif op == '(':
                        subStack.append(num)
                        break
                # print(sum(subStack))
                stack.append(sum(subStack))
        subStack = []
        while stack:
            num = stack.pop()
            op = '+'
            if stack:
                op = stack.pop()
            if op == '+':
                subStack.append(num)
            elif op == '-':
                subStack.append(-1 * num)
            elif op == '(':
                subStack.append(num)
                break

        return sum(subStack)

def tokenizeWithParens(s):
    token_list = []
    partial_num = []
    for c in s:
        if c in '+-*/()':
            if partial_num:
                token_list.append(''.join(partial_num))
                partial_num = []
            token_list.append(c)
        elif c.isdigit():
            partial_num += c
    if partial_num:
        token_list.append(''.join(partial_num))
    return token_list