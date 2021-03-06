# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        snail, hare = A, A
        while hare != None and hare.next != None:
            snail = snail.next
            hare = hare.next.next
        return snail
