class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if A[0] == 1:
             return 1
        sol = Solution()
        for i in range(len(A)-1):
            A[i+1] =  sol.getGCD(A[i], A[i+1])
            if A[i+1] == 1:
                return 1
        return 0

    def getGCD(self, a, b):
        ma = max(a,b)
        mi = min(a,b)
        if mi == 0:
            return ma
        if mi == 1:
            return mi
        return self.getGCD(ma%mi,mi)

if __name__ == '__main__':
    A= [1, 2, 4, 6, 8]
    print(Solution.solve(Solution, A))