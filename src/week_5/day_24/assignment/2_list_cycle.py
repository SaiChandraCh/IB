class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A == None:
            return
        snail, hare = A, A
        while True:
            snail = snail.next



if __name__ == '__main__':
    list = ListNode(1)
    temp = list
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(4)
    p = temp
    temp = temp.next
    temp.next = ListNode(5)
    temp = temp.next
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(7)
    temp = temp.next
    temp.next = ListNode(8)
    temp = temp.next
    temp.next = ListNode(9)
    temp.next = p
    Solution.detectCycle(Solution,list)
