def magic_squares():
    matrix = list(list())
    n = int(input())
    for rows in range(n):
        nums = input()
        matrix.append([int(x) for x in nums.split()])
    value = 0
    for i in range(n):
        value += matrix[0][i]

    output = True
    for i in range(1, n):
        sum = 0
        for j in range(n):
            sum += matrix[i][j]
        if sum!= value:
            return False
    sumA = 0
    sumB = 0
    sumMatrix = []
    for i in range(n):
        sumA += matrix[i][i]
        sumB += matrix[i][n-i-1]
    if sumA != sumB:
        return False
    if sumA != value:
        return False
    for i in range(n):
        sumC = 0
        for j in range(n):
            sumC += matrix[j][i]
        if sumC != value:
            return False

    return True
print(magic_squares())