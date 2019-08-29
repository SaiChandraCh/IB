class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        length = len(A)
        index = 0
        for i in range(length):
            if A[i] <= 0:
                A[i],A[index] = A[index],A[i]
                index += 1
        print(index)
        for i in range(index,length):
            if abs(A[i])+index-1 < length:
                A[abs(A[i])+index-1] = -A[abs(A[i])+index-1]
        print(A)
        for i in range(index,length):
            if A[i]>0:
                return i-index+1

        return length-index+1

if __name__ == '__main__':
    print(Solution.firstMissingPositive(Solution,[-1]))