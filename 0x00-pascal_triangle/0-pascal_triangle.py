def pascal_triangle(n):
    """
    Generates Pascal's triangle for a given positive integer n.
    Returns a list of lists of integers representing the triangle.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle

# Example usage:
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
