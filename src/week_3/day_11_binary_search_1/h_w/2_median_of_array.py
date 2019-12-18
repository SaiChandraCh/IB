class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        if len(A) <= 1 and len(B) <= 1:
            A.append(B)
            A.sort()
            return Solution.getMedian(Solution, A)
        median1 = Solution.getMedian(Solution, A)
        median2 = Solution.getMedian(Solution, B)

    def getMid(self,A):
        pass

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