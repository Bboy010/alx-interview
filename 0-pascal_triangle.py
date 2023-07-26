def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row of Pascal's triangle

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]  # First element of each row is always 1

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)  # Last element of each row is always 1
        triangle.append(current_row)

    return triangle

