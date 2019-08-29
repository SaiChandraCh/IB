class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @return a list of integers
    def solve(self, A, B, C, D):
        i = min(A,B,C)
        j = 0
        result = [i]
        length = 1
        print(result)
        while D>0:
            if result[j]*i < B:
                i *= result[j]
                result.append(i)
            elif result[length-1]*i > B:
                result.append(B)
            elif result[j]*i < C:
                pass
            D -= 1
        return result
if __name__ == '__main__':
    Solution.solve(Solution,2,3,5,D=5)