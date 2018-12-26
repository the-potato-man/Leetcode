class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def getShift(word):
            shifts = ''
            for i in range(1, len(word)):
                diff = ord(word[i]) - ord(word[i-1])
                if diff < 0:
                    diff += 26
                shifts = shifts + ',' + str(diff)
            return shifts
        
        groups = {}
        for word in strings:
            shift = getShift(word)
            if shift not in groups:
                groups[shift] = [word]
            else:
                groups[shift].append(word)
        
        res = []
        for val in groups.values():
            res.append(val)
        return res
