import timeit


def find3numbers(n, A):
    sol = []
    for i in range(n - 2):
        for j in range(i+1, n - 1):
            for k in range(j+1, n):
                x, y, z = A[i], A[j], A[k]
                if x < y < z:
                    sol.append([x, y, z])
    return sol


def find3numbers_2(n, A):
    sol = []
    for i in range(1, n - 1):
        y = A[i]
        x = min(A[:i])
        if x < y:
            z = max(A[i+1:])
            if y < z:
                sol.append([x, y, z])
    return sol


A = [12, 3, 53, 6, 3, 2, 556, 3, 2, 55, 67, 7, 10, 100, 101, 102]
n = len(A)

print(find3numbers(n, A))
print(find3numbers_2(n, A))
