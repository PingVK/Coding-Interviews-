"""
page 44 ，problem 4
对于一个每行每列递增的数组，判断整数是否存在
"""


def find_num(matrix: list, num: int) -> bool:
    if not matrix:
        return False
    if not (isinstance(matrix, list) and isinstance(matrix[0], list)):
        return False
    cols = len(matrix)
    rows = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            return False

    row, col = 0, cols-1
    while row < rows and col >= 0:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] < num:
            row += 1
        else:
            col -= 1
    return False


if __name__ == '__main__':
    number = 14
    case1 = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 14, 15]
    ]
    case2 = [
        [1, 3, 5, 6],
        [3, 5, 8, 9],
        [5, 8, 10, 12],
        [6, 9, 11, 13]
    ]
    case3 = [
        [5, 7, 8, 9],
        [7, 9, 10, 12],
        [8, 10, 11, 13],
        [10, 11, 13, 15]
    ]
    case4 = [
        [16, 17, 18, 19],
        [17, 18, 19, 20],
        [18, 19, 20, 21],
        [21, 22, 23, 24]
    ]
    case5 = [[]]
    cases = [case1, case2, case3, case4, case5]
    for case in cases:
        print(find_num(case, number))
