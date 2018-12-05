def print_spiral(number):
    """
    :param: integer whose spiral matrix is to be printed
    """
    size = number * 2 - 1
    # initialzing a matrix of required size
    matrix = [[0] * size for _ in range(size)]
    index = 0
    # value to be filled in matrix
    value = 1

    while (index < size):
        # print top row
        for i in range(index, size):
            matrix[index][i] = value

        # print last column
        for j in range(index, size):
            matrix[j][size - 1] = value

        # print bottom row
        for k in range(size - 1, index, -1):
            matrix[size - 1][k] = value

        # print first column
        for l in range(size - 1, index, -1):
            matrix[l][index] = value

        # updating indexes and values for next iteration
        index += 1
        # reducing size of matrix
        size -= 1
        # incrementing value to be printed
        value += 1

    return matrix

if __name__ == '__main__':
    result = print_spiral(4)
    print(result)
