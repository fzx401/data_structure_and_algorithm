def matrix_mut(mat1, mat2):
    """

    :param mat1: m*n
    :param mat2: n*k
    :return: m*k
    """
    if len(mat1[0]) != len(mat2):
        raise ValueError('Different dimension!')
    res = []
    tmp = []
    for m in range(len(mat1)):
        for k in range(len(mat2[0])):
            tmp.append(sum(mat1[m][n] * mat2[n][k] for n in range(len(mat1[0]))))
        res.append(tmp)
        tmp = []

    return res


mat1 = [[1, 2, 6], [3, 4, 2], [4, 4, 4]]
mat2 = [[5, 6], [7, 8], [19, 22]]
print(matrix_mut(mat1, mat2))