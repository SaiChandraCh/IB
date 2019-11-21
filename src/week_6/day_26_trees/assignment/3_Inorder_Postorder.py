# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    def buildTree(self, A, B):#A -> inorder, B -> postorder
        map = {}
        for i in range(len(A)):
            map[A[i]] = i
        return Solution.util(Solution, A, B, map, 0, len(A)-1, 0, len(B)-1)

    def util(self, inorder, postorder, inorder_map, in_start, in_end, po_start, po_end):
        if in_start>in_end or po_start>po_end:
            return None
        root = TreeNode(postorder[po_end])
        index = inorder_map[root.val]
        root.left = Solution.util(Solution, inorder, postorder, inorder_map, in_start, index-1, po_start, po_start+index-in_start-1)
        root.right = Solution.util(Solution, inorder, postorder, inorder_map, index+1, in_end, po_start+index-in_start, po_end-1)
        return root

if __name__ == '__main__':
    inorder, postorder = [9,3,15,20,7],[9,15,7,20,3]
    # [4,8,2,5,1,6,10,9,3,7],[8,4,5,2,10,9,6,7,3,1])
    root = Solution.buildTree(Solution, inorder, postorder)
    que = [root]
    while que:
        temp = que.pop(0)
        print(temp.val)
        if temp.left:
            que.append(temp.left)
        if temp.right:
            que.append(temp.right)