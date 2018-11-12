# 224. Basic Calculator

class Solution:
    def calculate(self,s):
        """
        :type s: str
        :rtype: int
        """
        tokens = tokenizeWithParens(s)
        stackWithOp = []
        for t in tokens:
            if t.isdigit():
                stackWithOp.append(int(t))
            elif t in '(+-':
                stackWithOp.append(t)
            elif t == ')':
                subStack = []
                while True:
                    num = stackWithOp.pop()
                    op = stackWithOp.pop()
                    if op == '+':
                        subStack.append(num)
                    elif op == '-':
                        subStack.append(-1 * num)
                    elif op == '(':
                        subStack.append(num)
                        break
                stackWithOp.append(sum(subStack))

        stack = [stackWithOp[0]]
        for i in range(1, len(stackWithOp), 2):
            op = stackWithOp[i]
            num = stackWithOp[i+1]
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-1 * num)

        return sum(stack)

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
            partial_num.append(c)
    if partial_num:
        token_list.append(''.join(partial_num))
    return token_list