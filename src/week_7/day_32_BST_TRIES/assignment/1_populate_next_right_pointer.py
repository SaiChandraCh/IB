class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        prev = root
        while prev:
            curr = prev
            while curr:
                if curr.left:
                    if curr.right:
                        curr.left.next = curr.right
                    else:
                        curr.left.next = self.getNext(self,curr)
                if curr.right:
                    curr.right.next = self.getNext(self,curr)
                curr = curr.next
            if prev.left:
                prev = prev.left
            elif prev.right:
                prev = prev.right
            else:
                prev = self.getNext(self,prev)
        return root

    def getNext(self,curr):
        temp = curr.next
        while temp:
            if temp.left:
                return temp.left
            if temp.right:
                return temp.right
            temp = temp.next
        return temp

if __name__ == '__main__':
    from util.binary_tree_util import binary_tree_util
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    A = [621367, 400139, 986434, 318453, 562082, 727076, None, 208016, 340383, 409269, None, 702531, 983736, 187691, None, None, 387077, None, 534779, 647033, 719463, 824451, None, None, None, 373900, None, 517606, None, None, None, None, 720965, None, 834145, None, None, None, None, None, None, None, None]
    root = Solution.connect(Solution,binary_tree_util.build(A))
    que = [root]
    while que:
        curr = que.pop(0)
        print(curr.val, curr.next.val if curr.next else None)
        if curr.left:
            que.append(curr.left)
        if curr.right:
            que.append(curr.right)