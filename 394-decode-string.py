class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def tokenize(s):
            sol = []
            partialNum = []
            for c in s:
                if c.isdigit():
                    partialNum.append(c)
                else:
                    sol.append(''.join(partialNum))
                    partialNum = []
                    sol.append(c)
            if partialNum:
                sol.append(''.join(partialNum))
            return sol
        
        tokens = tokenize(s)
        
        numStack = []
        solStack = []
        for c in tokens:
            if c == '[':
                solStack.append(c)
            elif c == ']':
                n = int(numStack.pop())
                subStr = ''
                while solStack[-1] != '[':
                    subStr = solStack.pop() + subStr
                solStack.pop() # removing '['
                temp = ''
                for i in range(n):
                    temp += subStr
                solStack.append(temp)
            elif c.isdigit():
                numStack.append(c)
            else: # c is a letter
                solStack.append(c)
        
        return ''.join(solStack)
