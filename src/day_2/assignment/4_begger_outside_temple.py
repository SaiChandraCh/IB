class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        beggers = [0 for _ in range(A)]
        for i in B:
            j = i[0]
            while j<=i[1]:
                beggers[j-1] += i[2]
                j+=1
        return beggers

if __name__ == '__main__':
    print(Solution.solve(Solution,A = 5, B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]))