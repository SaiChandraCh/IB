class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    res = []
    def __init__(self):
        Solution.res = []

    def subsetsWithDup(self, A):
        A.sort()
        Solution.util(self,A,[])
        Solution.res.sort()
        return Solution.res

    def util(self,A, rem):
        if len(A) == 0:
            if rem not in Solution.res:
                Solution.res.append(rem)
            return

        Solution.util(self,A[1:],rem)
        Solution.util(self,A[1:],rem+[A[0]])

if __name__ == '__main__':
    print(Solution.subsetsWithDup(Solution,[6, 6, 3, 3, 6, 5]))