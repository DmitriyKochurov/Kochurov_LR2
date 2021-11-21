import ast
import itertools
import copy
from math import floor, ceil

def matx_input(row):
    line = row
    ary = []
    for i in range(line):
        t = []
        for j in input().split():
            if j != " ":
                t.append(ast.literal_eval(j))
        ary.append(t)
    return ary


def matrix_print(result, row, column):
    line, columns = row, column
    for i in range(line):
        for j in range(columns):
            if result[i][j] == -0.0:
                print(0, end=" ")
            elif type(result[i][j]) == int or result[i][j] == 0:
                print(result[i][j], end=" ")
            elif type(result[i][j]) == float and result[i][j] != 0:
                if result[i][j] > 0:
                    print(floor(result[i][j] * 100) / 100.0, end=" ")
                else:
                    print(ceil(result[i][j] * 100) / 100.0, end=" ")
        print()


def matx_sum(m1, m2, row, col):
    line, columns = row, col
    append = []
    for i in range(line):
        temp = []
        for j in range(columns):
            temp.append(m1[i][j] + m2[i][j])
        append.append(temp)
    return append


def matx_number(m1, number_m):
    multiply = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a[0])):
            temp.append(m1[i][j] * number_m)
        multiply.append(temp)
    return multiply


def matx_element(l1, l2):
    result = 0
    for i in range(len(l1)):
        result += l1[i] * l2[i]
    return result


def matx_two(m1, m2):
    value = [[0 for row in range(len(m2[0]))] for column in range(len(m1))]
    for i in range(len(m1)):
        l1 = m1[i]
        for j in range(len(m2[0])):
            l2 = [m2[x][j] for x in range(len(m2))]
            value_range = matx_element(l1, l2)
            value[i][j] = value_range
    return value

def transe_main_diag(ary):
    return list(itertools.zip_longest(*ary))


def transe_side_diag(ary):
    new_matrix = [[ary[j][i] for j in range(len(ary))] for i in range(len(ary[0]) - 1, -1, -1)]
    result = []
    for i in range(len(new_matrix[0])):
        new_matrix[i] = new_matrix[i][::-1]
        result.append(new_matrix[i])
    return result


def transe_ver_line(ary):
    new_matrix = [[ary[j][i] for j in range(len(ary))] for i in range(len(ary[0]) - 1, -1, -1)]
    result = list(itertools.zip_longest(*new_matrix))
    return result


def transe_hor_line(ary):
    result = list(itertools.zip_longest(*ary[::-1]))
    result = list(itertools.zip_longest(*result))
    return result


def min(matx_min, i, j):
        return [row[:j] + row[j + 1:] for row in (matx_min[:i] + matx_min[i + 1:])]


def min_transe(ary):
    determ = det(ary)
    if len(ary) == 2:
        return [[ary[1][1] / determ, -1 * ary[0][1] / determ],
                [-1 * ary[1][0] / determ, ary[0][0] / determ]]
    cofactors = []
    for r in range(len(ary)):
        case = []
        for j in range(len(ary)):
            minored = min(ary, r, j)
            case.append(((-1) ** (r + j)) * det(minored))
        cofactors.append(case)
    cofactors = transe_main_diag(cofactors)
    for i in range(len(cofactors)):
        cofactors[i] = list(cofactors[i])
    for r in range(len(cofactors)):
        for j in range(len(cofactors)):
            cofactors[r][j] = int(cofactors[r][j]) / determ
    return cofactors

def det(matx_det):
    if len(matx_det) == 2:
        return matx_det[0][0] * matx_det[1][1] - matx_det[0][1] * matx_det[1][0]
    determ = 0
    for i in range(len(matx_det)):
        determ += ((-1) ** i) * matx_det[0][i] * det(min(matx_det, 0, i))
    return determ


while True:
    print("""1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
0. Exit""")
    choice = int(input("Your choice:"))
    choice = int(input('Your choice:'))
    if choice == 1:
        matx, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matx_input(matx)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matx_input(p)
        if matx != p and n != q:
            print("The operation cannot be performed.")
        else:
            c = matx_sum(a, b, matx, n)
            matrix_print(c, matx, n)
    elif choice == 2:
        m, n = map(int, input("Enter size of matrix:").split())
        print("Enter matrix:")
        a = matx_input(matx)
        number = float(input("Enter constant:"))
        c = matx_number(a, number)
        print("The result is:")
        matrix_print(c, matx, n)
    elif choice == 3:
        matx, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matx_input(m)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matx_input(p)
        c = matx_two(a, b)
        print("The result is:")
        matrix_print(c, matx, q)
    elif choice == 4:
        print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line.""")
        choice = int(input("Your choice:"))
        if choice == 1:
            matx, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(matx)
            c = transe_main_diag(a)
            print('The result is:')
            matrix_print(c, n, matx)
        elif choice == 2:
            matx, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(matx)
            c = transe_side_diag(a)
            print('The result is:')
            matrix_print(c, n, matx)
        elif choice == 3:
            matx, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(m)
            c = transe_ver_line(a)
            print('The result is:')
            matrix_print(c, matx, n)
        elif choice == 4:
            matx, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(m)
            c = transe_hor_line(a)
            print('The result is:')
            matrix_print(c, matx, n)
        elif choice == 5:
            matx, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(matx)
            c = det(a)
            print('The result is:')
            print(c)
        elif choice == 6:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(matrix)
            c = det(a)
            print(c)
            if c != 0:
                d = min_transe(a)
                print('The result is:')
                matrix_print(d, matrix, n)
            else:
                print("This matrix doesn't have an inverse.")
        elif choice == 0:
            break