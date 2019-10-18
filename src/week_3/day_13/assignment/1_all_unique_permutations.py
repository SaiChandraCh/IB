class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    def permute(self, A):
        Solution.res = []
        Solution.util(Solution, A, [])
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
                Solution.util(Solution,A[:i]+A[i+1:],choosen+[A[i]])

if __name__ == '__main__':
    print(Solution.permute(Solution,[ 1, 2, 3, 4, 5,6,7,8]))