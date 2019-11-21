class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        while A and B:
            if A.val < B.val:
                temp = A.val
                A = A.next
            else:
                temp = B.val
                B = B.next

            if not C:
                C = ListNode(temp)
                c = C
            else:
                c.next = ListNode(temp)
                c = c.next
        while A:
            c.next = A.next
            A = A.next
            c = c.next

        while B:
            c.next = B.next
            B = B.next
            c = c.next
        return  C
if __name__ == '__main__':
    A = ListNode(1)
    Solution.mergeTwoLists(Solution,A,B)