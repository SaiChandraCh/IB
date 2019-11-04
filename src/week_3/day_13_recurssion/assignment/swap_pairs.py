class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head:
            return
        if not head.next:
            return head
        temp = head.next
        head.next = temp.next
        temp.next = head
        head = temp
        temp = temp.next
        if temp:
            temp.next = Solution.swapPairs(Solution,temp.next)
        return head

if __name__ == '__main__':
    root = ListNode(1)
    temp = root
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(5)
    node = Solution.swapPairs(Solution,root)
    while node:
        print(node.val)
        node = node.next