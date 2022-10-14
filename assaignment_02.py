
# Solution of System of Linear Equations-SLEs. The Inverse Matrix, lower and upper triangular matrix using LU Decomposition method

def swap(a, b):
    c = a
    a = b
    b = c
    return [a, b]

def printMatrix(mat, n):
    for i in range(n):
        for j in range(n):
            print('   {}   '.format(mat[i][j]), end='')
        print('')

def NGEM():
    print('Naïve Gaussian Elimination is A method to solve simultaneous linear equations of the form [A][X]=[C]')
    print('Division by zero, error could be occurred.')
    n = int(input('Enter the dimension or number of unknowns: '))
    print('Now we need matrix A of size {}*{} and then matrix C of size {}*1'.format(n, n, n))
    print('Matrix A of size {}*{}:'.format(n, n))
    A = []
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    print('Matrix C of size {}*1:'.format(n))
    C = []
    for i in range(n):
        C.append(float(input()))
    # Forward Elimination
    for i in range(n):
        for j in range(i):
            val = A[i][j]/A[j][j]
            for k in range(n):
                A[i][k] -= A[j][k]*val
            C[i] -= C[j]*val
    ans = []
    for i in range(n):
        ans.append(0)
    # Back Substitution
    ind = n-1
    while ind >= 0:
        val = 0
        for i in range(ind+1, n):
            val += A[ind][i]*ans[i]
        val = C[ind]-val
        ans[ind] = val/A[ind][ind]
        ind -= 1
    print('')
    print('The Solutions using Naïve Gaussian Elimination:')
    print(ans)
    print('')

def GEwPP():
    print('Gaussian Elimination with Partial Pivoting is A method to solve simultaneous linear equations of the form [A][X]=[C]')
    n = int(input('Enter the dimension or number of unknowns: '))
    print('Now we need matrix A of size {}*{} and then matrix C of size {}*1'.format(n, n, n))
    print('Matrix A of size {}*{}:'.format(n, n))
    A = []
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    print('Matrix C of size {}*1:'.format(n))
    C = []
    for i in range(n):
        C.append(float(input()))
    # Forward Elimination
    for i in range(n):
        row = i
        mx = abs(A[i][i])
        for j in range(i, n):
            if mx < abs(A[j][j]):
                mx = abs(A[j][j])
                row = j
        for j in range(n):
            A[i][j], A[row][j] = map(float, list(swap(A[i][j], A[row][j])))
        C[i], C[row] = map(float, list(swap(C[i], C[row])))
        for j in range(i+1, n):
            val = (A[j][i]/A[i][i])
            for k in range(n):
                A[j][k] -= val*A[i][k]
            C[j] -= val*C[i]
    ans = []
    for i in range(n):
        ans.append(0)
    # Back Substitution
    ind = n - 1
    while ind >= 0:
        val = 0
        for i in range(ind + 1, n):
            val += A[ind][i] * ans[i]
        val = C[ind] - val
        ans[ind] = val / A[ind][ind]
        ind -= 1
    print('')
    print('The Solutions using Gaussian Elimination with Partial Pivoting:')
    print(ans)
    print('')

def LTMat(A, n):
    # Forward Elimination
    B = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        B.append(row)
    for i in range(n):
        B[i][i] = 1
    for i in range(n):
        for j in range(i, n):
            B[j][i] = A[j][i]/A[i][i]
        for j in range(i + 1, n):
            val = (A[j][i] / A[i][i])
            for k in range(n):
                A[j][k] -= val * A[i][k]
    return B

def UTMat(A, n):
    # Forward Elimination
    for i in range(n):
        for j in range(i):
            val = A[i][j] / A[j][j]
            for k in range(n):
                A[i][k] -= A[j][k] * val
    return A

def IM(A, n):
    L = LTMat(A, n)
    U = UTMat(A, n)
    I = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        I.append(row)
    for col in range(n):
        Z = []
        for i in range(n):
            Z.append(0)
        for ind in range(n):
            val = 0
            for i in range(ind):
                val += L[ind][i] * Z[i]
            cur = 0
            if ind == col:
                cur = 1
            val = cur - val
            Z[ind] = val
        B = []
        for i in range(n):
            B.append(0)
        ind = n - 1
        while ind >= 0:
            val = 0
            for i in range(ind + 1, n):
                val += U[ind][i] * B[i]
            val = Z[ind] - val
            B[ind] = val / U[ind][ind]
            ind -= 1
        for i in range(n):
            I[i][col] = B[i]
    print('')
    print('The Inverse Matrix:')
    printMatrix(I, n)

def LUDecomposition():
    n = int(input('Enter the dimension of the Square Matrix: '))
    print('Matrix A of size {}*{}:'.format(n, n))
    A = []
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    lo = LTMat(A, n)
    print('')
    print('The Upper Triangular Matrix:')
    printMatrix(lo, n)
    print('')
    hi = UTMat(A, n)
    print('The Lower Triangular Matrix:')
    printMatrix(hi, n)
    print('')
    IM(A, n)
    print('')

print("Assalamualaikum ")
while True:
	
    print('Click 1 for Naïve Gaussian Elimination method')
    print('Click 2 for Gaussian Elimination with Partial pivoting')
    print('Click 3 for Lower, Upper Triangular and Inverse Matrix using LU Decomposition')
    print('Click 0 to Exit')
    choice = int(input("Enter your choice :"))
    if choice == 0:
        exit()
    if choice == 1:
        NGEM()
    elif choice == 2:
        GEwPP()
    elif choice == 3:
        LUDecomposition()
    else:
        print('Wrong Choice! Try again.')