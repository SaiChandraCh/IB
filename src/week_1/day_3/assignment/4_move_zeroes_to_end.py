class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        length = len(A)
        i = 0
        count = 0
        while i<length:
            if A[i] == 0:
                A.pop(i)
                i-=1
                length -= 1
                count += 1
            i += 1

        for i in range(count):
            A.append(0)
        return A

if __name__ == '__main__':
    print(Solution.solve(Solution,[ 34, 8, 14, 71, 78, 62, 0, 0, 84, 64, 0, 43 ]))