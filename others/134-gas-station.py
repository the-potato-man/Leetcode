'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
'''

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
