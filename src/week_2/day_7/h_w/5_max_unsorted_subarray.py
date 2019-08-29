class Solution:
	# @param A : list of integers
	# @return a list of integers
    def subUnsort(self, A):
        length = len(A)
        for start in range(length-1):
            if A[start] > A[start+1]:
                break

        for end in range(length-1,0,-1):
            if A[end] < A[end-1]:
                break

        if length == 1 or (start == length-2 and end == 1):
            return [-1]
        min, max = A[start], A[end]

        for i in A[start:end+1]:
            if i < min:
                min = i
            elif i > max:
                max = i

        for i in range(start):
            if A[i] > min:
                start = i
                break

        # for i in range(length-1,end+2,-1):
        #     if A[i] < max:
        #         end = i
        #         break
        i = length-1
        while i >= end+1:
            if A[i] < max:
                end = i
                break
            i -= 1

        return [start,end]

if __name__ == '__main__':
    print(Solution.subUnsort(Solution,
                             # [1,2,3]))
                             # [4, 15, 4, 4, 15, 18, 20]))
                             # [1, 2, 2, 3, 3, 5, 6, 6, 14, 17, 18, 17, 18, 15, 15, 17, 19, 14, 19, 18]))#9 19
                             # [1, 2, 3, 5, 6, 13, 15, 16, 17, 13, 13, 15, 17, 17, 17, 17, 17, 19, 19]))
                            # [10,12,20,30,25,40,32,31,35,50,60]))
                             [1, 1, 10, 10, 15, 10, 15, 10, 10, 15, 10, 15]))#4 10
                            #  [3, 3, 4, 5, 5, 9, 11, 13, 14, 15, 15, 16, 15, 20, 16]))
                             # A=[1, 2, 3, 4, 5]))
                             # [1, 3, 2, 4, 5]))
                             # [5, 7, 13, 9, 3, 2, 8, 1, 10, 12]))