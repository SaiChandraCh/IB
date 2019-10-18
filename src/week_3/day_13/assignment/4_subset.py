class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    subset = []
    def subsets(self, A):
        self.subset = []
        A.sort()
        Solution.util(Solution,A,[],{})
        Solution.subset.sort(key=lambda x:(x,len(x)))
        return self.subset

    def util(self, A, rem, visited):
        if len(A) == 0:
            
            self.subset.append(rem)
            return

        x = A[0]
        if x not in visited:
            visited[x] = True
            self.util(self,A[1:],rem)
            self.util(self,A[1:],rem+[x])

if __name__ == '__main__':
    A = Solution
    print(A.subsets(A,[1,2,2]))
