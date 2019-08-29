class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        len_a = len(A)
        len_b = len(B)
        for index,val in enumerate(A):
            left = 0
            right = len_b-1
            while left<=right:
                mid = left + (right-left)//2
                if val == B[mid]:
                    break
                elif val > B[mid]:
                    left = mid+1
                else:
                    right = mid-1
            if B[mid] > val:
                b = mid-1 if mid>1 else 0
            elif B[mid] < val:
                b = mid+1 if mid<len_b-1 else len_b-1


if __name__ == '__main__':
    print(Solution.findMedianSortedArrays(Solution,A = [1,4,5],B = [2,3]))