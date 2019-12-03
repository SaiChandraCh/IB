class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = 100
        prime = [False] * (n + 2)
        primesquare = [False] * (n * n + 2)
        a = [0] * n
        Solution.SieveOfEratosthenes(n, prime, primesquare, a)
        ans = 1
        i = 0
        while (1):
            if (a[i] * a[i] * a[i] > n):
                break
            cnt = 1
            while (n % a[i] == 0):
                n = n / a[i]
                cnt = cnt + 1

            ans = ans * cnt
            i += 1

        n = int(n)
        if (prime[n] == True):
            ans = ans * 2

        elif (primesquare[n] == True):
            ans = ans * 3

        elif (n != 1):
            ans = ans * 4

        return ans

    def SieveOfEratosthenes(n, prime, primesquare, a):
        for i in range(2, n + 1):
            prime[i] = True

        for i in range((n * n + 1) + 1):
            primesquare[i] = False

        prime[1] = False

        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                i = p * 2
                while (i <= n):
                    prime[i] = False
                    i += p
            p += 1

        j = 0
        for p in range(2, n + 1):
            if (prime[p] == True):
                # Storing primes in an array
                a[j] = p
                primesquare[p * p] = True
                j += 1

if __name__ == '__main__':
    A= [1, 2, 3, 4, 5]
    # A = [10, 20]
    print(Solution.solve(Solution, A))
