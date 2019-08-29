class Solution:
	# @param A : list of integers
	# @return a list of integers
    def subUnsort(self, A):
        length = len(A)
        indices = set()
        i = 0
        if length > 2:
            while i < length-2:
                if (A[i]+A[i+2])//2 != A[i+1] :
                    if A[i+2] < A[i]:
                        indices.add(i+2)
                    elif A[i+1] > A[i+2]:
                        indices.add(i+1)
                    else:
                        indices.add(i)
                i += 1
            return list(indices) if len(indices)>0 else [-1]
        elif length == 2:
            return [-1] if A[0]<=A[1] else [0,1]
        elif length == 1:
            return A


if __name__ == '__main__':
    print(Solution.subUnsort(Solution,[ 1, 1, 10, 10, 15, 10, 15, 10, 10, 15, 10, 15 ]))

