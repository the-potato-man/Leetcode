'''
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
'''

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
