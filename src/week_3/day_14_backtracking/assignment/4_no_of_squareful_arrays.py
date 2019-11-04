class Solution:
    # @param A : list of integers
    # @return an integer
    res = 0
    def __init__(self):
        Solution.res = 0

    def solve(self, A):
        Solution.permute(Solution,A,[])
        return Solution.res

    def permute(self,A,choosen):
        length = len(A)
        if length == 0:
            squareFull = Solution.isSquareFull(Solution, choosen)
            if squareFull:
                Solution.res += 1
            return

        visited = {}
        for i in range(length):
            if A[i] not in visited:
                visited[A[i]] = True
                Solution.permute(self, A[:i] + A[i + 1:], choosen + [A[i]])

    def isSquareFull(self,A):
        length = len(A)-1
        if length < 0:
            return False

        if length == 0:
            root = A[0]**1/2
            if root != int(root):
                return False

        for i in range(length):
            root = (A[i]+A[i+1])**(1/2)
            if root != int(root):
                return False
        return True

if __name__ == '__main__':
    print(Solution.solve(Solution,
                   # [41])
                   [861623468, 361474260, 657794791, 992545490, 921729504, 818255817, 866864601, 925498858, 921493879])
                   # [ 2, 2, 2 ])
                    )