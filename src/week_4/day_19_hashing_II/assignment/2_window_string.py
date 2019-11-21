class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def minWindow(self, A, B):
        length_A = len(A)
        length_B = len(B)
        if length_A == 0 or length_B == 0 or length_B > length_A:
            return ""
        min_length = length_A + 1
        freq_B = {}
        for i in B:
            if i not in freq_B:
                freq_B[i] = 1
            else:
                freq_B[i] += 1

        start = -1
        freq_window = {}
        temp = length_B
        for i in range(len(A)):
            if A[i] in freq_B:
                start = i
                break
        result = ""
        for curr in range(start,len(A)):
            if A[curr] in freq_window:
                freq_window[A[curr]] += 1
            else:
                freq_window[A[curr]] = 1
            if A[curr] in freq_B and freq_window[A[curr]] <= freq_B[A[curr]]:
                temp -= 1
            if temp <= 0 and A[curr] in freq_B and freq_window[A[curr]] >= freq_B[A[curr]]:
                while A[start] not in freq_B or freq_window[A[start]] > freq_B[A[start]]:
                    if A[start] in freq_B:
                        freq_window[A[start]] -= 1
                    start += 1
                if min_length > curr-start:
                    result = A[start:curr+1]
                    min_length = curr-start
        return result


if __name__ == '__main__':
    print(Solution.minWindow(Solution,
                             "ab","a"))
                             # "THEADOBECODEBANC","ABC"))