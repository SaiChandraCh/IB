class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        start = 0
        B = []
        length = len(A)
        for i, val in enumerate(A):
            if val > 0:
                start = i
                break

        for i in range(start, length):
            if A[i] < 0:
                B.append(A[start:i])
                start = i + 1
        B.append(A[start:])

        max = sum(B[0])
        maxLen = len(B[0])
        resIndex = 0
        result = B[0]
        length = len(B)
        for i in range(1,length):
            if sum(B[i]) > max:
                max = sum(B[i])
                result = B[i]
                maxLen = len(B[i])
                resIndex = i
            elif sum(B[i]) == max and len(B[i]) > maxLen:
                maxLen = len(B[i])
                result = B[i]
                resIndex = i
            elif sum(B[i]) == max and len(B[i]) == maxLen and resIndex > i:
                maxLen = len(B[i])
                result = B[i]
                resIndex = i
        return result

if __name__ == '__main__':
    print(Solution.maxset(Solution,[1, 2, 5, -7, 2, 3,9, -1, 100]))