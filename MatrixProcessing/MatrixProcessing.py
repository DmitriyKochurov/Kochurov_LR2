import ast
import itertools

def matx_input(row):
    line = row
    matx = []
    for i in range(line):
        t = []
        for j in input().split():
            if j != " ":
                t.append(ast.literal_eval(j))
        matx.append(t)
    return matx


def matrix_print(result, row, column):
    line, columns = row, column
    for i in range(line):
        for j in range(columns):
            print(result[i][j], end=' ')
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
            temp.append(float(m1[i][j]) * float(number_m))
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

def transe_main_diag(matrix):
    result = list(itertools.zip_longest(*matrix))
    return result


def transe_side_diag(matrix):
    new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]
    result = []
    for i in range(len(new_matrix[0])):
        new_matrix[i] = new_matrix[i][::-1]
        result.append(new_matrix[i])
    return result


def transe_ver_line(matrix):
    new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]
    result = list(itertools.zip_longest(*new_matrix))
    return result


def transe_hor_line(matrix):
    result = list(itertools.zip_longest(*matrix[::-1]))
    result = list(itertools.zip_longest(*result))
    return result


while True:
    print("""1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
0. Exit""")
    choice = int(input("Your choice:"))
    choice = int(input('Your choice:'))
    if choice == 1:
        m, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matx_input(m)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matx_input(p)
        if m != p and n != q:
            print("The operation cannot be performed.")
        else:
            c = matx_sum(a, b, m, n)
            matrix_print(c, m, n)
    elif choice == 2:
        m, n = map(int, input("Enter size of matrix:").split())
        print("Enter matrix:")
        a = matx_input(m)
        number = float(input("Enter constant:"))
        c = matx_number(a, number)
        print("The result is:")
        matrix_print(c, m, n)
    elif choice == 3:
        m, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matx_input(m)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matx_input(p)
        c = matx_two(a, b)
        print("The result is:")
        matrix_print(c, m, q)
    elif choice == 4:
        print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line.""")
        choice = int(input("Your choice:"))
        if choice == 1:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(m)
            c = transe_main_diag(a)
            print('The result is:')
            matrix_print(c, n, m)
        elif choice == 2:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(m)
            c = transe_side_diag(a)
            print('The result is:')
            matrix_print(c, n, m)
        elif choice == 3:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(m)
            c = transe_ver_line(a)
            print('The result is:')
            matrix_print(c, m, n)
        elif choice == 4:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(m)
            c = transe_hor_line(a)
            print('The result is:')
            matrix_print(c, m, n)
        elif choice == 0:
            break