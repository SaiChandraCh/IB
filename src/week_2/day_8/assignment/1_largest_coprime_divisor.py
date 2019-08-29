class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
    def cpFact(self, A, B):
        for x in range(A,1,-1):
            if A%x == 0:
                x1 = min(x,B)
                x2 = max(x,B)
                while x2%x1>1:
                    x1, x2 = x2 % x1, x1
                if x2%x1 == 1:
                    return x
        return 1


if __name__ == '__main__':
    print(Solution.cpFact(Solution,
                          24,36)) # 1
                          # 30,12)) # 5
                          # 90, 47)) # 2
                          #   2,2)) # 2
                          # 2, 3))  # 2