class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if n == 1:
            return 0 if gas[0] >= cost[0] else -1
        
        start = 0
        end = 1
        
        petrol = gas[0] - cost[0]
        while start != end or petrol < 0:
            while start != end and petrol < 0:
                petrol = petrol - (gas[start] - cost[start])
                start = (start + 1) % n
                if start == 0:
                    return -1
            petrol = petrol + gas[end] - cost[end]
            end = (end + 1) % n
        
        return start
