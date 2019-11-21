class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        que = [A,None]
        while que and B > 0:
            curr = que.pop(0)
            if curr:
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            else:
                if not que:
                    break
                que.append(None)
                B -= 1
        result = ""
        while que:
            curr = que.pop(0)
            if curr:
                result += str(curr.val)
        return result


if __name__ == '__main__':
    A = [8 ,1 ,8 ,9 ,5 ,3 ,6 ,1 ,4 ,3 ,4 ,8 ,None ,None ,None ,None ,None ,None ,None ,None ,None ,None ,None ,None ,None]
    from src.util.binary_tree_util import binary_tree_util
    print(Solution.solve(Solution,binary_tree_util.build(A), 2))