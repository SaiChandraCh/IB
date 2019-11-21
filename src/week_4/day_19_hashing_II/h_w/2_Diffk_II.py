class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def diffPossible(self, A, B):
        map = {}
        map_repeated = {}
        print(map)
        print(map_repeated)
        count = 0
        for i in range(len(A)):
            if A[i] in map and i != map[A[i]]:
                print(A[i])
                while map_repeated[A[i]] > 1:
                    count += 1
                    map_repeated[A[i]] -= 1
                count += 1
        return count

    def diffPossible_b(self, A, B):
        count = 0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i] == A[j]+B:
                    count += 1
        return count

if __name__ == '__main__':
    A = \
        [ 66, 37, 46, 56, 49, 65, 62, 21, 7, 70, 13, 71, 93, 26, 18, 84, 96, 65, 92, 69, 97, 47, 6, 18, 17, 47, 28, 71, 70, 24, 46, 58, 71, 21, 30, 44, 78, 31, 45, 65, 16, 3, 22, 54, 51, 68, 19, 86, 44, 99, 53, 24, 40, 92, 38, 81, 4, 96, 1, 13, 45, 76, 77, 8, 88, 50, 89, 38, 60, 61, 49, 25, 10, 80, 49, 63, 95, 74, 29, 27, 52, 27, 40, 66, 38, 22, 85, 22, 91, 98, 19, 20, 78, 77, 48, 63, 27 ]
        # [1,5,3]
    B = \
        31
        # 2
    print(Solution.diffPossible(Solution, A, B))
    print(Solution.diffPossible_b(Solution, A, B))