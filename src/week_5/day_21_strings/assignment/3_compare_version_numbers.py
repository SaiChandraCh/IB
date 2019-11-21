class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
    def compareVersion(self, A, B):
        version_1 = A.split(".")
        version_2 = B.split(".")
        len1 = len(version_1)
        len2 = len(version_2)
        for i in range(len1-1,-1,-1):
            if int(version_1[i])==0:
                version_1.pop(len1-1)
                len1 -= 1
            else:
                break

        for i in range(len2-1,-1,-1):
            if int(version_2[i])==0:
                version_2.pop(len2-1)
                len2 -= 1
            else:
                break

        length = len1 if len1<len2 else len2
        for i in range(length):
            if i< len1 and i< len2:
                if int(version_1[i]) < int(version_2[i]):
                    return -1
                elif int(version_1[i]) > int(version_2[i]):
                    return 1
        if len1>len2:
            return 1
        if len1<len2:
            return -1
        return 0

if __name__ == '__main__':
    print(Solution.compareVersion(Solution,
                                  "01","1.0"))
                                  # "01.13","1.13.4"))
                                    # 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4