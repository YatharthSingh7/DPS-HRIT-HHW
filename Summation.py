def series_1(x: float, n: int) -> float:
    # 1 + x + x^2 + ... + x^n
    if x == 1:
        return n + 1
    return (1 - x ** (n + 1)) / (1 - x)

def series_2(x: float, n: int) -> float:
    # 1 - x + x^2 - x^3 + ... ± x^n
    if x == 1:
        return 1 if n % 2 == 0 else 0
    return (1 - (-x) ** (n + 1)) / (1 + x)

def series_3(x: float, n: int) -> float:
    # x + x^2 + x^3 + ... + x^n
    if x == 1:
        return n
    return (x - x ** (n + 1)) / (1 - x)

def series_4(x: float, n: int) -> float:
    # x - x^2 + x^3 - x^4 + ... ± x^n
    if x == 1:
        return 1 if n % 2 == 1 else 0
    return (x - (-x) ** (n + 1)) / (1 + x)

def get_input() -> tuple[float, int]:
    while True:
        try:
            x = float(input("Enter value for x: "))
            n = int(input("Enter non-negative integer value for n: "))
            if n < 0:
                raise ValueError("n must be non-negative")
            return x, n
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

def main() -> None:
    print("Choose the series to calculate sum for:")
    print("1) 1 + x + x^2 + ... + x^n")
    print("2) 1 - x + x^2 - x^3 + ... ± x^n")
    print("3) x + x^2 + x^3 + ... + x^n")
    print("4) x - x^2 + x^3 - x^4 + ... ± x^n")

    choice = input("Enter choice (1-4): ").strip()
    x, n = get_input()

    if choice == '1':
        result = series_1(x, n)
    elif choice == '2':
        result = series_2(x, n)
    elif choice == '3':
        result = series_3(x, n)
    elif choice == '4':
        result = series_4(x, n)
    else:
        print("Invalid choice.")
        return

    print(f"Sum of the chosen series is: {result}")

if __name__ == "__main__":
    main()
