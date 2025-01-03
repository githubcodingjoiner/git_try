def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence: {fibonacci(n)}")