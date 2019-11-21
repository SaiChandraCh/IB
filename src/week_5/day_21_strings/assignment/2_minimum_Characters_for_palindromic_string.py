class Solution:
	# @param A : string
	# @return an integer
    def solve(self, A):
        length = len(A)
        flag = False
        k = length//2 if length%2 != 0 else (length-1)//2
        i, j = k-1, k+1
        while k > 0 and i >= 0 and j < length:
            print(i,k,j,A[i],A[k],A[j])
            if A[i] == A[j]:
                i -= 1
                j += 1
                flag = True
            else:
                k -= 1
                j -= 1
                i -= 1
                # k -= i
                # i, j = k - 1, k + 1

        if k == length//2:
            return 0
        if flag:
            return length-j
        if not flag:
            return length-(j+1)

if __name__ == '__main__':
    print(Solution.solve(Solution,
                         # "ABC"))
                         # "AACECAAAA"))
                         "BANANA"))
