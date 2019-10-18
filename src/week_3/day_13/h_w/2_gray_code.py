class Solution:
    # @param A : integer
    # @return a list of integers
    res = []
    def grayCode(self, A):
        Solution.res = []
        Solution.util(Solution,A,0,0)
        return Solution.res

    def util(self,A,val,decimal_position):
        if A == 0:
            Solution.res.append(val)
            return
        Solution.util(Solution,A-1,2*val,decimal_position+1)
        Solution.util(Solution,A-1,2*val+1,decimal_position+1)

if __name__ == '__main__':
    Solution.grayCode(Solution,10)
    print(Solution.res)