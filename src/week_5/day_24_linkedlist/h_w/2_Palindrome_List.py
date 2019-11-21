# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
    def lPalin(self, A):
        snail, hare = A, A
        p1 = A
        while hare:
            snail = snail.next
            if not hare.next:
                break
            hare = hare.next.next
        p2 = Solution.reverse(Solution,snail)

        while p1 and p2 and p1.val != p2.val:
            p1 = p1.next
            p2 = p2.next


    def reverse(self, curr):
        prev = None
        start = curr
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        start.next = curr
        return prev
if __name__ == '__main__':
    A = ListNode(1)
    temp = A
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(1)
    # temp = temp.next
    # temp.next = ListNode(4)
    # temp = temp.next
    # temp.next = ListNode(5)
    # temp = temp.next
    # temp.next = ListNode(6)
    # temp = temp.next
    # temp.next = ListNode(7)
    # temp = temp.next
    print(Solution.lPalin(Solution,A))