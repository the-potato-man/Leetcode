'''
Sort a nearly sorted (or K sorted) array
Given an array of n elements, where each element is at most k away from its target position, 
devise an algorithm that sorts in O(n log k) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.
'''

import heapq
def sortKSortedArray(nums, k):
    n = len(nums)
    pq = []
    for i in range(k+2):
        heapq.heappush(pq, nums[i])
    
    res = []
    for i in range(k+2, n):
        heapq.heappush(pq, nums[i])
        res.append(heapq.heappop(pq))
    
    while pq:
        res.append(heapq.heappop(pq)) 

    return res

def test():
    nums1 = [6, 5, 3, 2, 8, 10, 9]
    k1 = 3

    nums2 = [10, 9, 8, 7, 4, 70, 60, 50]
    k2 = 4

    print(sortKSortedArray(nums1, k1))
    print(sortKSortedArray(nums2, k2))

test()
