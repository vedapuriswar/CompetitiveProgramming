
def LCS(p, q):
    n = len(p)
    m = len(q)
    if n == 0 or m == 0:
        result = 0
    elif p[n-1] == q[m-1]:
        result = 1 + LCS(p[:n-1], q[:m-1])
    elif p[n-1] is not q[n-1]:
        temp1 = LCS(p[:n-1], q)
        temp2 = LCS(p, q[:m-1])
        result = max(temp1, temp2)
    return result


print(LCS(['a', 'b', 'c'], ['b', 'c']))