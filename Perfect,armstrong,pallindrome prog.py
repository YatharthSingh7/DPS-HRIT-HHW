class NumberAnalyzer:
    def __init__(self, number: int):
        if number < 0:
            raise ValueError("Number must be non-negative.")
        self.number = number

    def is_perfect(self) -> bool:
        num = self.number
        if num < 2:
            return False
        divisors_sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        return divisors_sum == num

    def is_armstrong(self) -> bool:
        digits = str(self.number)
        power = len(digits)
        total = sum(int(d) ** power for d in digits)
        return total == self.number

    def is_palindrome(self) -> bool:
        s = str(self.number)
        return s == s[::-1]

    def analyze(self) -> dict:
        return {
            "perfect": self.is_perfect(),
            "armstrong": self.is_armstrong(),
            "palindrome": self.is_palindrome()
        }

def get_input() -> int:
    while True:
        try:
            val = int(input("Enter a non-negative integer: "))
            if val < 0:
                raise ValueError("Number must be non-negative.")
            return val
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

def show_examples():
    print("\n--- Example Numbers Analysis (limit 5) ---")
    examples = [6, 153, 370, 371, 407]  # Limited to 5
    for ex in examples:
        a = NumberAnalyzer(ex)
        res = a.analyze()
        print(f"\nNumber: {ex}")
        print(f"  Perfect: {'Yes' if res['perfect'] else 'No'}")
        print(f"  Armstrong: {'Yes' if res['armstrong'] else 'No'}")
        print(f"  Palindrome: {'Yes' if res['palindrome'] else 'No'}")
    print("\nNote: No known number is all three (perfect, Armstrong, palindrome) simultaneously (checked examples).")

def main():
    while True:
        print("\nSelect an option:")
        print("1) Analyze your own number")
        print("2) View example numbers analysis (5 examples)")
        print("3) Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            num = get_input()
            analyzer = NumberAnalyzer(num)
            results = analyzer.analyze()
            print(f"\nAnalysis for number {num}:")
            print(f"Is Perfect Number? {'Yes' if results['perfect'] else 'No'}")
            print(f"Is Armstrong Number? {'Yes' if results['armstrong'] else 'No'}")
            print(f"Is Palindrome? {'Yes' if results['palindrome'] else 'No'}")
        elif choice == "2":
            show_examples()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
