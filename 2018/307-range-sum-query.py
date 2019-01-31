# https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/python-well-commented-solution-using-segment-trees

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = None


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def buildTree(nums, left, right):
            if left > right:
                return
            if left == right:
                root = Node(left, right)
                root.total = nums[left]
                return root

            mid = (left + right) // 2
            root = Node(left, right)
            root.left = buildTree(nums, left, mid)
            root.right = buildTree(nums, mid+1, right)
            root.total = root.left.total + root.right.total
            return root

        self.root = buildTree(nums, 0, len(nums)-1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def helper(node, i, val):
            if node.start == node.end and node.start == i:
                node.total = val
                return

            mid = (node.start + node.end) // 2

            if i <= mid:
                helper(node.left, i, val)
            else:
                helper(node.right, i, val)

            node.total = node.left.total + node.right.total

        helper(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def helper(node, i, j):
            if node.start == i and node.end == j:
                return node.total

            mid = (node.start + node.end) // 2

            if j <= mid:
                return helper(node.left, i, j)
            elif i >= mid + 1:
                return helper(node.right, i, j)
            else:
                return helper(node.left, i, mid) + helper(node.right, mid+1, j)

        return helper(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
