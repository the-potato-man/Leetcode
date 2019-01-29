'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''

import string

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def isOneAway(word1, word2):
            numDiff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    numDiff += 1
                if numDiff > 1:
                    break
            return True if numDiff == 1 else False
        
        # Getting neighbors, so don't have to traverse entire dictionary
        def getNeighbors(word, wordListSet):
            neighbors = []
            for i in range(len(word)):
                for c in string.ascii_lowercase: # a-z
                    temp = word[:i] + c + word[i+1:]
                    if temp in wordListSet:
                        neighbors.append(temp)
            return neighbors
        
        # Changing dictionary's word list to a set for faster lookup 
        wordListSet = set()
        for word in wordList:
            wordListSet.add(word)
        
        visited = set()
        visited.add(beginWord)
        queue = [(beginWord, 1)]
            
        while queue:
            temp, steps = queue.pop(0)
            if temp == endWord:
                return steps
            neighbors = getNeighbors(temp, wordListSet)
            for word in neighbors:
                if isOneAway(temp, word) and word not in visited:
                    queue.append((word, steps + 1))
                    visited.add(word)        
        return 0
