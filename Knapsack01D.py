n = 0
c = 0
w = [0]
v = [0]
arr = [[-1 for column in range(n)] for row in range(c)]


def knapsack(n, c):
    if arr[n][c] != -1:
        return arr[n][c]
    if n is 0 or c is 0:
        result = 0
    elif w[n] > c:
        result = knapsack(n-1, c)
    else:
        temp1 = knapsack(n-1, c)
        temp2 = v[n] = knapsack(n-1, c - w[n])
        result = max(temp1, temp2)
    arr[n][c] = result
    return result

