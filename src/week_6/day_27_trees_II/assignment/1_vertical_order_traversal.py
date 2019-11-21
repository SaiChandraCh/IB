# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers

    def verticalOrderTraversal(self, A):
        map = {} # result map
        hd_map ={} # horizontal distance of each node => distance from the root
        que = [root]
        hd_map[root] = 0
        map[0] = [root.val]
        while que:
            curr = que.pop(0)
            if curr.left:
                que.append(curr.left)
                hd_map[curr.left] = hd_map[curr]-1
                if hd_map[curr.left] not in map:
                    map[hd_map[curr.left]] = [curr.left.val]
                else:
                    map[hd_map[curr.left]].append(curr.left.val)

            if curr.right:
                que.append(curr.right)
                hd_map[curr.right] = hd_map[curr]+1
                if hd_map[curr.right] not in map:
                    map[hd_map[curr.right]] = [curr.right.val]
                else:
                    map[hd_map[curr.right]].append(curr.right.val)
        result = []
        for i in sorted(map):
            result.append(map[i])
        print(result)
        return result

if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)

    # root = TreeNode(0)
    # root.left = TreeNode(8)
    # root.right = TreeNode(1)
    # root.right.left = TreeNode(3)
    # root.right.right = TreeNode(2)
    # root.right.left.right = TreeNode(4)
    # root.right.left.right.right = TreeNode(7)
    # root.right.right.left = TreeNode(5)
    # root.right.right.left.left = TreeNode(6)

    root = TreeNode(0)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)

    root.left.left.left.right = TreeNode(7)
    root.left.left.left.right.left = TreeNode(10)
    root.left.left.left.right.right = TreeNode(8)
    root.left.left.right.left = TreeNode(6)
    root.left.left.right.left.left = TreeNode(11)
    root.left.left.right.left.right = TreeNode(9)
    print(Solution.verticalOrderTraversal(Solution,root))