class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        length = len(A)
        indices = []
        for i, val in enumerate(A):
            print(i,val)
        # for i in range(1, length):
        #     # print(i-1,i,A[i - 1], A[i],A[i - 1] > A[i])
        #     if A[i - 1] > A[i]:
        #         indices.append(i - 1)
        # return indices if len(indices)>0 else [-1]

if __name__ == '__main__':
    print(Solution.subUnsort(Solution,[ 1, 5, 3, 4, 2 ]))#[ 1, 3, 2, 4, 5 ]