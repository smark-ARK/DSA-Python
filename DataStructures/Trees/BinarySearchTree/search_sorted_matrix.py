def search(matrix, target, n):
    i = 0
    j = n - 1
    while j >= 0 and i < n:
        if matrix[i][j] == target:
            print(f"Found at position: ({i}, {j})")
            return
        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    print("Not Found")
    return


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
search(matrix, 5, 3)
