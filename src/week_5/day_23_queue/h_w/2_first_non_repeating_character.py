class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        char_freq = [-1 for _ in range(26)]
        que = []
        result = ""
        for i in A:
            char_freq[ord(i) - 97] += 1
            que.append(i)
            while len(que) > 0 and char_freq[ord(que[0]) - 97] != 0:
                que.pop(0)
            if len(que) == 0:
                result += "#"
            else:
                result += que[0]
        return result

if __name__ == '__main__':
    # A = "abadbc"
    A = "abcabc"
    print(Solution.solve(Solution,A))