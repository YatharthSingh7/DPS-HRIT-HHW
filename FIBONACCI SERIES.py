from typing import Generator

def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """
    Generates the Fibonacci series up to n terms.
    Uses a generator for efficient memory usage.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def get_term_count() -> int:
    """
    Prompts the user for a positive integer (number of Fibonacci terms).
    """
    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms to display: "))
            if n <= 0:
                raise ValueError("Number of terms must be positive.")
            return n
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main() -> None:
    print("🔢 Fibonacci Series Generator")
    n_terms = get_term_count()

    print(f"\nFirst {n_terms} terms of the Fibonacci series:")
    series = list(fibonacci_generator(n_terms))
    print(", ".join(map(str, series)))

if __name__ == "__main__":
    main()
