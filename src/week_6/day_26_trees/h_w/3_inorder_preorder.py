class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    def buildTree(self, A, B):
        # A - preorder
        # B - inorder
        map = {}
        for i in range(len(B)):
            map[B[i]] = i
        return Solution.util(self, B, A, map, 0, len(A)-1, 0, len(B)-1)

    def util(self, inorder, preorder, inorder_map, in_start, in_end, pre_start, pre_end):
        if in_start>in_end or pre_start>pre_end:
            return
        root = TreeNode(preorder[pre_start])
        index = inorder_map[root.val]
        root.left = Solution.util(Solution,inorder, preorder, inorder_map, in_start, index-1, pre_start+1, pre_start+index-in_start)
        root.right = Solution.util(Solution, inorder, preorder, inorder_map, index+1, in_end, pre_start+index-in_start+1, pre_end)
        return root

if __name__ == '__main__':
    A = [3,9,20,15,7] #preorder
    B = [9,3,15,20,7] #inorder
    root = Solution.buildTree(Solution,A,B)
    que = [root]
    while que:
        temp = que.pop(0)
        print(temp.val)
        if temp.left:
            que.append(temp.left)
        if temp.right:
            que.append(temp.right)