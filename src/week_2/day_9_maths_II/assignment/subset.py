if __name__ == '__main__':
    N = 3
    A = [1,2,3]
    for i in range(8):
        for j in range(N):
            if (i & (1<<j)):
                print(A[j],end=",")
        print()
