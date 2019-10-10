class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers

    visited = {}
    top_view = []
    def solve(self, A):
        self.top_view = []
        self.visited = {}
        self.util(self, A, self.visited, 0)
        return self.top_view

    def util(self, root, visited, curr_level):
        if root == None:
            return None
        if curr_level not in visited:
            visited[curr_level] = 1
            self.top_view.append(root.val)
        self.util(self, root.left, visited, curr_level - 1)
        self.util(self, root.right, visited, curr_level + 1)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    print(Solution.solve(Solution,root))

    root = TreeNode(9)
    root.left = TreeNode(6)
    root.right = TreeNode(17)
    root.left.left = TreeNode(23)
    root.left.right = TreeNode(7)
    print(Solution.solve(Solution,root))