class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ''
        for word in sentence:
            s = s + word + ' '
        
        curr = 0
        for i in range(rows):
            curr += cols
            if s[curr % len(s)] == ' ':
                curr += 1
            else:
                while curr > 0 and s[(curr-1) % len(s)] != ' ':
                    curr -= 1
        
        return curr // len(s)
