class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        map = {}
        length = len(A)
        res = []
        for i in range(length):
            for j in range(i+1,length):
                temp = A[i]+A[j]
                if temp not in map:
                    map[A[i]+A[j]] = [i,j]
                else:
                    if map[temp][0] != i and  map[temp][0] != j and  map[temp][1] != i  and  map[temp][1] != j :
                        res.append([map[temp][0],map[temp][1],i, j])
        if len(res) == 0:
            return []
        else:
            result = [res[0][0], res[0][1], res[0][2], res[0][3]]
            for index in range(1,len(res)):
                temp = [res[index][0], res[index][1], res[index][2], res[index][3]]
                if result[0] > temp[0]:
                    result = temp
                    continue
                elif result[0] == temp[0]:
                    if result[1] > temp[1]:
                        result = temp
                        continue
                    elif result[1] == temp[1]:
                        if result[2] > temp[2]:
                            result = temp
                            continue
                    elif result[2] == temp[2]:
                        if result[3] > temp[3]:
                            result = temp
                            continue
        return result

if __name__ == '__main__':
    print(Solution.equal(Solution, [ 3, 4, 7, 1, 2, 9, 8 ]))
