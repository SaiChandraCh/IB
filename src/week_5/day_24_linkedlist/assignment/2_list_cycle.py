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
        while snail and hare:
            snail = snail.next
            hare = hare.next.next
            if snail == hare:
                break
        print(snail.val, hare.val)
        snail = A
        while snail != hare:
            print(snail.val,hare.val)
            snail = snail.next
            hare = hare.next
            print(snail.val,hare.val)

        return snail

if __name__ == '__main__':
    list = ListNode(1)
    temp = list
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    p = temp
    temp.next = ListNode(5)
    temp = temp.next
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(7)
    temp.next = p
    print(Solution.detectCycle(Solution,list).val)
