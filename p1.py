def mat_mult(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
    return result

def mat_expo(base, exp):
    size = len(base)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)] 
    while exp > 0:
        if exp % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        exp //= 2
    return result

def factorial_matrix(n):
    if n == 0 or n == 1:
        return 1

    T = [
        [1, 1],
        [0, 1]
    ]
    T_n_minus_1 = mat_expo(T, n - 1)
    return T_n_minus_1[0][1]

while True:
    try:
        num = int(input("Enter a non-negative integer (or -1 to exit): "))
        if num == -1:
            break
        elif num < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"The factorial of {num} is {factorial_matrix(num)}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
