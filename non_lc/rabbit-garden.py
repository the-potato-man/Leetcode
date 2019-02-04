class Solution:
    def getNumCarrotsEaten(self, garden):
        # Counter for the number of carrots eaten by the rabbit
        self.carrotsEaten = 0

        # Returns the starting position in the center of the garden
        # If there is no exact center, returns the square closest to the center with the highest carrot count
        def getStartPosition(garden):
            n = len(garden)
            mid = n // 2

            if n % 2 != 0: return mid, mid
            maxCarrots = float('-inf')
            startCoordinates = (None, None)
            for r, c in [(mid, mid), (mid-1, mid), (mid, mid-1), (mid-1, mid-1)]:
                if garden[r][c] > maxCarrots:
                    maxCarrots = garden[r][c]
                    startCoordinates = r, c

            return startCoordinates
        
        # Traverses through the garden, updating the carrotsEaten counter, and removing carrots from the garden
        def moveAndEat(startR, startC, garden):
            self.carrotsEaten += garden[startR][startC]
            garden[startR][startC] = 0
            while True:
                numCarrots, r, c = chooseNextArea(startR, startC, garden)
                if numCarrots <= 0: break
                self.carrotsEaten += garden[r][c]
                garden[r][c] = 0
                startR, startC = r, c
        
        # Checks that the given row and col are within the bounds of the garden
        def isWithinGarden(r, c, garden):
            n = len(garden)
            m = len(garden[0])
            return 0 <= r < n and 0 <= c < m

        # Given the current position, returns the neighboring position with the highest carrot count
        # Returns an invalid position, if there are no neighboring squares with carrots
        def chooseNextArea(r, c, garden):
            nextR = -1
            nextC = -1
            nextNumCarrots = float('-inf')

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                if not isWithinGarden(r+dr, c+dc, garden): continue
                numCarrots = garden[r+dr][c+dc]
                if numCarrots > nextNumCarrots:
                    nextR = r + dr
                    nextC = c + dc
                    nextNumCarrots = numCarrots

            return nextNumCarrots, nextR, nextC

        if len(garden) == len(garden[0]) == 1: return garden[0][0]
        r, c = getStartPosition(garden)
        moveAndEat(r, c, garden)
        return self.carrotsEaten

    def test(self):
        garden1 = [
                [5, 7, 8, 6, 3],
                [0, 0, 7, 0, 4],
                [4, 6, 3, 4, 9],
                [3, 1, 0, 5, 8]
            ]
        garden2 = [[3]]
        garden3 = [
                [5, 0],
                [0, 6],
            ]
        garden4 = [
                [5, 2],
                [0, 6],
            ]
        garden5 = [
                [5, 7, 0, 6, 3],
                [0, 0, 7, 0, 4],
                [4, 6, 3, 0, 9],
                [3, 1, 0, 5, 8],
                [3, 1, 0, 5, 8]
            ]

        print(self.getNumCarrotsEaten(garden1))
        print(self.getNumCarrotsEaten(garden2))
        print(self.getNumCarrotsEaten(garden3))
        print(self.getNumCarrotsEaten(garden4))
        print(self.getNumCarrotsEaten(garden5))
        

def main():        
    s = Solution()
    s.test()

main()
