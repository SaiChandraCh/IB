# class Solution:
#     # @param A : list of integers
#     # @return an integer
#
#
#     def solve(self, A):
#         sum = 0
#         dup = 0
#         A.sort()
#         length = len(A)
#         for i in range(length):
#             for j in range(i+1,length):
#                 if (j+1<length and A[j] == A[j+1]) or A[i] == A[j]:
#                     dup += 1
#                     continue
#                 print(A[i],A[j],j-i+dup)
#                 sum += (A[j]-A[i])*(j-i+dup)
#         return sum
#
# if __name__ == '__main__':
#     print(Solution.solve(Solution,
#                          [3, 10, 2, 3, 8, 1, 10, 4] #Expected - 1787
#                          # [7, 8, 6, 4, 6] #Expected - 66
#                          # [5,3,1,4]
#                          # [5,4,2,6,3,9,7]
#                          ))

# python for finding max min difference
# from all subset of given set

MOD = 1000000007;

# function for sum of max min difference
def maxMin(arr, n):
    # sort all numbers
    arr.sort()

    # iterate over array and with help of
    # horner's rule calc max_sum and min_sum
    min_sum = 0
    max_sum = 0
    print(arr)
    for i in range(0, n):
        max_sum = 2 * max_sum + arr[n - 1 - i];
        max_sum %= MOD;
        min_sum = 2 * min_sum + arr[i];
        min_sum %= MOD;
        print(max_sum,min_sum)

    return (max_sum - min_sum + MOD) % MOD;


# Driver Code
arr = [3, 10, 2, 3, 8, 1, 10, 4]
n = len(arr)
print(maxMin(arr, n))

# This code is contributed by Sam007.
