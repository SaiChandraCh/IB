class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
    res = []
    def combinationSum(self, A, B):
        Solution.res = []
        A.sort()
        Solution.util(self,A,B,[])
        return Solution.res

    def util(self,set,desired_sum, sub_set):
        length = len(set)
        if desired_sum == 0:
            Solution.res.append(sub_set)
            return
        if length == 0:
            return
        visited = {}
        for i in range(length):
            if set[i] not in visited:
                visited[set[i]] = True
                if desired_sum - set[i] >= 0 and (not sub_set or sub_set and sub_set[-1] <= set[i]):
                        Solution.util(Solution,set,desired_sum-set[i],sub_set+[set[i]])

if __name__ == '__main__':
    print(Solution.combinationSum(Solution,[8, 10, 6, 11, 1, 16, 8], 28))