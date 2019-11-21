class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        que = [0]
        i = 1
        length = 0
        while A>length:
            que.append(10 * que[i-1] + 1)
            length += 1
            if A>length:
                que.append(10 * que[i-1] + 2)
                length += 1
            else:
                break
            if A>length:
                que.append(10 * que[i-1] + 3)
                length += 1
            else:
                break
            i += 1
        return que[1:]

if __name__ == '__main__':
    print(Solution.solve(Solution,15))