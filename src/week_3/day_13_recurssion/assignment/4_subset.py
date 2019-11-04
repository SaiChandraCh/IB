class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    subset = []
    def subsets(self, A):
        A.sort()
        Solution.util(Solution,A,[])
        # Solution.subset.sort(key=lambda x:(x,len(x)))
        # return self.subset

    def util(self, A, rem):
        if len(A) == 0:
            print(rem)
            self.subset.append(rem)
            return

        self.util(self,A[1:],rem)
        self.util(self,A[1:],rem+[A[0]])

if __name__ == '__main__':
    A = Solution
    print(A.subsets(A,
                    [3, 10, 2, 3, 8, 1, 10, 4]
                    # [7, 8, 6, 4, 6]
                    # [1,2,2]
                    ))
