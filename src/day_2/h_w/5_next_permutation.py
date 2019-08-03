class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        changed = False
        sum = 0
        if len(A)>1:
            for i in (length-1,0,-1):
                if A[i] > A[i-1]:
                    A[i],A[i-1] = A[i-1],A[i]
                    changed = True
                    break
            if not changed:
                A = sorted(A)
            for i in A:
                sum += sum*10 + i
        return sum
if __name__ == '__main__':
    Solution.nextPermutation()