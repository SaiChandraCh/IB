class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        length = len(A)
        i = 0
        while i < length:
            if i != A[i]:
                temp = A[A[i]]
                A[A[i]] = A[i]
                A[i] = temp
                count += 1
                i -= 1
            i += 1
        return count


if __name__ == '__main__':
    print(Solution.solve(Solution,[2, 1, 0, 4, 3]))