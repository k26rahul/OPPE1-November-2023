def matrix_type(M):
    n = len(M)

    isDiagonal, isScalar, isIdentity = True, True, True

    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] != 0:
                isDiagonal = False
            if i == j and M[i][j] != M[0][0]:
                isScalar = False
            if i == j and M[i][j] != 1:
                isIdentity = False

    if not isDiagonal:
        return 'non-diagonal'

    if isIdentity:
        return 'identity'

    return 'scalar' if isScalar else 'diagonal'


assert matrix_type([[1, 0], [0, 1]]) == 'identity'
assert matrix_type([[1, 2, 5], [2, 3, 5], [1, 4, 9]]) == 'non-diagonal'
assert matrix_type([[2, 0, 0], [0, 2, 0], [0, 0, 2]]) == 'scalar'
assert matrix_type([[1, 0, 1], [0, 1, 0], [0, 0, 1]]) == 'non-diagonal'
assert matrix_type([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 'identity'
assert matrix_type([[1, 0, 0, 0], [0, 1, 0, 0], [
    0, 0, 1, 0], [0, 0, 0, 2]]) == 'diagonal'
assert matrix_type([[1, 0, 0, 0], [0, 2, 0, 0], [
    0, 0, 3, 0], [0, 0, 0, 4]]) == 'diagonal'
