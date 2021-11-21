import constant as constant

while True:
    limns_a1 = list(input("Please, input line and columns matrix A: \n"))
    column_a1 = int(limns_a1[0])
    line_a1 = int(limns_a1[2])
    matx_a1 = []
    line_true_a = 0
    for i in range(column_a1):
        matx_a1.append(list(map(int, input().split())))
    for height in range(len(matx_a1)):
        if len(matx_a1[height]) == line_a1:
            line_true_a += 1
    if line_true_a == column_a1:
        constant = int(input())
        break
    else:
        print("Please, try again")
        result = []
        for i in range(column_a1):
            result.append([0] * line_a1)
        for i in range(len(matx_a1)):
            for j in range(len(matx_a1[0])):
                result[i][j] = matx_a1[i][j] * constant
        for matrix_result in range(len(result)):
            print(*result[matrix_result])