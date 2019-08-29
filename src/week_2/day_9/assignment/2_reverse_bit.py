class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        temp = A
        count = 0
        while temp != 0:
            temp = temp >> 1
            count += 1
        temp = A
        while temp > 0 and temp%2 == 0:
            temp = temp//2
            count += 1

        print(bin(A))
        for i in range(32):
            A = A<<1
            print(A,bin(A))
        return A

if __name__ == '__main__':
    print(Solution.reverse(Solution,4294967294))
    # 4294967294 - 2147483647
    # 4 - 536870912
    # 3 - 3221225472
    # 2 - 1073741824
    # 1 - 2147483648