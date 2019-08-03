class Solution:
    # @param A : tuple of integers
    # @return a list of integers repeated, expected
    def repeatedNumber(self, A):
        diff = 0
        sqDiff = 0
        for i in range(1,len(A)+1):
            diff += i - A[i-1]
            sqDiff += i*i-A[i-1]*A[i-1]
        sum = sqDiff//diff
        return [(sum-diff)//2 , (sum+diff)//2]

if __name__ == '__main__':
    print(Solution.repeatedNumber(Solution,[3,1,2,5,3]))