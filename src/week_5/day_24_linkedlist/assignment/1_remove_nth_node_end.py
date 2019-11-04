class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    counter = 0
    found = False
    res = None

    def removeNthFromEnd(self, A, B):
        self.counter = B+1
        A = self.util(self,A)
        print("counter : ", self.counter,"root : ",A)

        return A.next if self.counter > 0 and A!= None else A

    def util(self,A):
        if A == None:
            return None
        self.util(self, A.next)
        self.counter -= 1
        if self.counter == 0:
            self.found = True
            A.next = A.next.next
        return A


if __name__ == '__main__':
    arr = [20 , 380 , 349 , 322 , 389 , 424 , 429 , 120 , 64 , 691 , 677 , 58 , 327 , 631 , 916 , 203 , 484 , 918 , 596 , 252 , 509 , 644 , 33 , 460]
    list = ListNode(arr[0])
    temp = list
    for i in range(1,len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next

    A = Solution.removeNthFromEnd(Solution, list, 30)
    print(A)
    temp = A
    while temp != None:
        print(temp.val)
        temp = temp.next