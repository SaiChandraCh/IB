# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        curr = A
        prev = None
        i = 1
        while i < B:
            prev = curr
            curr = curr.next
            i += 1
        if curr and C>B:
            temp = Solution.reverse(Solution,curr,C-B)
            if prev:
                prev.next = temp
            else:
                return temp
        return A

    def reverse(self, curr, c):
        prev = None
        start = curr
        while curr and c>=0:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            c -= 1
        start.next = curr
        return prev

if __name__ == '__main__':
    A = ListNode(1)
    temp = A
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(5)
    temp = temp.next
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(7)
    temp = temp.next
    head = Solution.reverseBetween(Solution,A,1,3) # 1 4 3 2 5 6 7
    # Solution.reverseBetween(Solution,A,2,5) # 1 5 4 3 2 6 7
    # Solution.reverseBetween(Solution,A,3,6) # 1 2 6 5 4 3 2 7

    while head:
        print(head.val)
        head = head.next