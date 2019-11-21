# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # def solve(self, A):
        # left_view = [A.val]
        # sub = []
        # que = [A]
        # que.append(None)
        # while True:
        #     curr = que.pop(0)
        #     if curr:
        #         if curr.left:
        #             que.append(curr.left)
        #             sub.append(curr.left)
        #         if curr.right:
        #             que.append(curr.right)
        #             sub.append(curr.right)
        #     else:
        #         if len(que) == 0:
        #             return left_view
        #         left_view.append(sub[0].val)
        #         sub = []
        #         que.append(None)
    max_level = 0
    left_view = []
    def solve(self, A):
        self.util(self,A,1)
        return self.left_view

    def util(self,root,curr_level):
        if root == None:
            return None
        if curr_level > self.max_level:
            self.left_view.append(root.val)
            self.max_level += 1
        self.util(self,root.left,curr_level+1)
        self.util(self,root.right,curr_level+1)

if __name__ == '__main__':
    A = {}
    print(0 not in A,A)
    A[0] = 1
    print(0 not in A,A)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # root.left.left.left = TreeNode(8)

    # root = TreeNode(9)
    # root.left = TreeNode(6)
    # root.right = TreeNode(17)
    # root.left.left = TreeNode(23)
    # root.left.right = TreeNode(7)
    # print(Solution.solve(Solution,root))