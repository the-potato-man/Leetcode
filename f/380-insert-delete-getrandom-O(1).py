# Design a data structure that supports all following operations in average O(1) time.

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx = self.pos[val]
            lastNum = self.nums[-1]
            # Remove from self.nums and self.pos
            self.nums[idx] = lastNum
            self.pos[lastNum] = idx         
            self.nums.pop()
            del self.pos[val]
            return True
        return False        
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
