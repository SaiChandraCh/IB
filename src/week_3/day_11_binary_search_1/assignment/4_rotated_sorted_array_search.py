class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        length = len(A)
        if B == A[0]:
            return 0
        elif B == A[length-1]:
            return length-1
        left = 0
        right = length-1
        pivot = 0
        while left <= right:
            mid = left + (right-left)//2
            if mid+1 < length and A[mid]>A[mid+1]:
                pivot = mid+1
                break
            elif A[left] <= A[mid]:
                left = mid+1
            else:
                right = mid-1

        if pivot>0 and B >= A[0] and B <= A[pivot-1]:
            right = pivot-1
            left = 0
        elif B > A[pivot] and B < A[length-1]:
            left = pivot
            right = length-1
        else:
            return -1

        while left <= right:
            mid = left + (right-left)//2
            if A[mid] < B:
                left = mid+1
            elif A[mid] > B:
                right = mid-1
            else:
                return mid
        return -1

if __name__ == '__main__':
    print(Solution.search(Solution,
                          [1,2,3,4],
                          3))