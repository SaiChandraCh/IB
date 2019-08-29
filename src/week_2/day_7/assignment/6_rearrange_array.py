class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        N = len(A)
        print("length : ", N)
        for i in range(N):
            if A[i] < N:
                prev = A[i]
                j = i
                while A[j]< N and A[A[j]]< N:
                    index = A[j]
                    A[j] = A[A[j]] + N
                    j = index
                A[j] = prev + N

        for i in range(N):
            A[i] -= N

        return A

if __name__ == '__main__':
    print(Solution.arrange(Solution,
                           # [1,0]))
                           # [2, 1, 3, 0]))# => 3 1 0 2
                           [ 4,0,2,1,3]))
                           # [1, 2, 7, 0, 9, 3, 6, 8, 5, 4]))
