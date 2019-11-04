class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        Solution.res = 0

    def permute(self, A):
        Solution.util(self, A, [])
        return self.res

    res = []
    def util(self,A,choosen):
        length = len(A)
        if length == 0:
            self.res.append(choosen.copy())
            return
        visited = {}
        for i in range(length):
            if A[i] not in visited:
                visited[A[i]] = True
                Solution.util(self,A[:i]+A[i+1:],choosen+[A[i]])

if __name__ == '__main__':
    print(Solution.permute(Solution,[ 1, 1, 2]))