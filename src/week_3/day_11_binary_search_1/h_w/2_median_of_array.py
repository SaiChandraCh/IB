class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        odd = False
        if (len(A)+len(B))%2 != 0:
            odd = True
        return Solution.util(Solution,A,B,odd)

    def util(self,A,B,odd):
        if len(A) == len(B) == 2:
            if odd:
                return min(A[-1],B[-1])
            return (max(A[0],B[0])+min(A[-1],B[-1]))/2

        median_a = Solution.getMedian(Solution,A)
        median_b = Solution.getMedian(Solution,B)
        if median_a > median_b:
            if len(A) == 2:
                return Solution.util(Solution,A,B[len(B)//2-1:] if len(B)>3 else B[len(B)//2:], odd)
            if len(B) == 2:
                return Solution.util(Solution, A[:len(A) // 2 + 1], B, odd)
            return Solution.util(Solution,A[:len(A)//2+1],B[len(B)//2-1:] if len(B)>3 else B[len(B)//2:], odd)
        else:
            if len(A) == 2:
                return Solution.util(Solution, A, B[:len(B) // 2 + 1], odd)
            if len(B) == 2:
                return Solution.util(Solution, A[len(A) // 2-1:] if len(A)>3 else A[len(A) // 2:], B, odd)
            return Solution.util(Solution, A[len(A) // 2-1:] if len(A)>3 else A[len(A) // 2:], B[:len(B) // 2+1], odd)

    def getMedian(self,A):
        length = len(A)
        if length % 2 != 0:
            return A[length//2]
        return (A[(length)//2-1]+A[length//2])/2

if __name__ == '__main__':
    print(Solution.findMedianSortedArrays(Solution,
                                          A = [16,20,23,50,54,65],
                                          B = [60,72,85,93])
                                          # A = [4,20,32,50,55,61],
                                          # B = [1,15,22,30,70])
                                          # A = [1,4,5],
                                          # B = [2,3])
          )