class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        pass

if __name__ == '__main__':
    head = ListNode(1)
    temp = head
    # temp = temp.next
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(5)
    Solution.reverseList(Solution,head)