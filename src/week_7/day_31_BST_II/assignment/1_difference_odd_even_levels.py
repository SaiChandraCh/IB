# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        que = [A,None]
        even_sum, odd_sum, curr_sum = 0, 0, 0
        flag = True
        while que:
            curr = que.pop(0)
            if curr:
                curr_sum += curr.val
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            else:
                if not que:
                    break
                que.append(None)
                if flag:
                    odd_sum += curr_sum
                else:
                    even_sum += curr_sum
                curr_sum = 0
                flag = not flag
        return odd_sum-even_sum