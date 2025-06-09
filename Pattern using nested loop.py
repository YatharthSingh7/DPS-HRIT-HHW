def pattern_1(rows: int = 5) -> None:
    """
    Pattern-1: Increasing asterisks
    *
    **
    ***
    ****
    *****
    """
    for i in range(1, rows + 1):
        print("*" * i)

def pattern_2(rows: int = 5) -> None:
    """
    Pattern-2: Decreasing numbers
    12345
    1234
    123
    12
    1
    """
    for i in range(rows, 0, -1):
        print("".join(str(num) for num in range(1, i + 1)))

def pattern_3(rows: int = 5) -> None:
    """
    Pattern-3: Increasing alphabets
    A
    AB
    ABC
    ABCD
    ABCDE
    """
    for i in range(1, rows + 1):
        print("".join(chr(65 + j) for j in range(i)))

def main() -> None:
    patterns = {
        "1": pattern_1,
        "2": pattern_2,
        "3": pattern_3,
        "4": None,  # special option to print all
    }
    print("Select a pattern to print:")
    print("1. Pattern-1 (Increasing asterisks)")
    print("2. Pattern-2 (Decreasing numbers)")
    print("3. Pattern-3 (Increasing alphabets)")
    print("4. Print all patterns")

    choice = input("Enter choice (1-4): ").strip()
    rows = 5  # default rows, can be modified

    if choice in patterns:
        print()
        if choice == "4":
            print("Pattern 1:")
            pattern_1(rows)
            print("\nPattern 2:")
            pattern_2(rows)
            print("\nPattern 3:")
            pattern_3(rows)
        else:
            patterns[choice]()  # Call single pattern
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

