import math

class NumberClassifier:
    def __init__(self, number: int):
        if number < 1:
            raise ValueError("Number must be a positive integer greater than 0.")
        self.number = number

    def is_prime(self) -> bool:
        """
        Check if the number is prime.
        1 is neither prime nor composite by convention.
        """
        n = self.number
        if n == 1:
            return False  # Special case
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        limit = int(math.isqrt(n))
        for i in range(3, limit + 1, 2):
            if n % i == 0:
                return False
        return True

    def classify(self) -> str:
        if self.number == 1:
            return "Neither prime nor composite"
        return "Prime" if self.is_prime() else "Composite"

def get_positive_int() -> int:
    while True:
        try:
            val = int(input("Enter a positive integer (>0): "))
            if val <= 0:
                raise ValueError("Number must be greater than zero.")
            return val
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main() -> None:
    num = get_positive_int()
    classifier = NumberClassifier(num)
    classification = classifier.classify()
    print(f"\nNumber {num} is: {classification}")

if __name__ == "__main__":
    main()
