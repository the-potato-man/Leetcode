class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def isValid(r, c):
            return r >= 0 and c >= 0 and r < m and c < n
        
        sol = []
        land2id = {} # position to island id
        numIslands = 0
        islandId = 0
        
        for r, c in positions:
            overlap = set()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nextR = r + dr
                nextC = c + dc
                pos = nextR * n + nextC
                if isValid(nextR, nextC) and pos in land2id:
                    overlap.add(land2id[pos])
            
            key = r * n + c
            if not overlap:
                numIslands += 1
                islandId += 1                
                land2id[key] = islandId
            elif len(overlap) == 1:
                land2id[key] = next(iter(overlap))
            else:
                rootId = next(iter(overlap))
                for pos, landId in land2id.items():
                    if landId in overlap:
                        land2id[pos] = rootId
                land2id[key] = rootId
                numIslands -= (len(overlap) - 1)
            sol.append(numIslands)
            
        return sol
