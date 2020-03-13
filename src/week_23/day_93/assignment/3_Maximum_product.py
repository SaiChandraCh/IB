class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return A[0]
        A.sort()
        sum1, sum2 = 0, 0
        for i in range(len(A)):
            if (sum2+A[i])*sum1 > (sum1+A[i])*sum2:
                sum2 += A[i]
            else:
                sum1 += A[i]
        print(sum1, sum2)
        return sum1 * sum2


if __name__ == '__main__':
    print(Solution.solve(Solution, [ 1, 6, 5, 7, 1, 2, 8, 0, 5, 5 ]))
