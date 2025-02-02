"""Matrix exponentiation-based factorial calculation."""

def mat_mult(matrix_a, matrix_b):
    """Multiplies two square matrices matrix_a and matrix_b."""
    size = len(matrix_a)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def mat_expo(base, exponent):
    """Computes matrix exponentiation using exponentiation by squaring."""
    size = len(base)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    while exponent > 0:
        if exponent % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        exponent //= 2
    return result

def factorial_matrix(n):
    """Computes factorial using matrix exponentiation."""
    if n in {0, 1}:
        return 1
    transformation_matrix = [[1, 1], [0, 1]]
    return mat_expo(transformation_matrix, n - 1)[0][1]

def main():
    """Handles user input and calls factorial computation."""
    while True:
        try:
            num = int(input("Enter a non-negative integer (or -1 to exit): "))
            if num == -1:
                break
            if num < 0:
                print("Please enter a non-negative integer.")
            print(f"The factorial of {num} is {factorial_matrix(num)}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
