def spiral_matrix(matrix, r, c):
    k, l = (
        0,
        0,
    )
    while k < r and l < c:
        for i in range(k, c):
            print(matrix[k][i], end=" ")
        k += 1
        for i in range(k, r):
            print(matrix[i][c - 1], end=" ")
        c -= 1
        if k < r:
            for i in range(c - 1, l - 1, -1):
                print(matrix[r - 1][i], end=" ")
            r -= 1
        if l < c:
            for i in range(r - 1, k - 1, -1):
                print(matrix[i][l], end=" ")
            l += 1


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
spiral_matrix(matrix, 4, 4)
