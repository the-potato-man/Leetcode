class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0

class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
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
                 
        self.numRow = len(matrix) if matrix else 0
        self.numCol = len(matrix[0]) if matrix else 0
        
        self.rootList = [None] * self.numRow
        for i in range(self.numRow):
            self.rootList[i] = buildTree(matrix[i], 0, self.numCol - 1)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
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
            
        helper(self.rootList[row], col, val)       

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
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
        
        res = 0
        for i in range(row1, row2 + 1):
            res += helper(self.rootList[i], col1, col2)
        return res 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
