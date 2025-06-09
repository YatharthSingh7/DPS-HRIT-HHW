from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class NumberSet:
    numbers: Tuple[float, float, float]

    def largest(self) -> float:
        return max(self.numbers)

    def smallest(self) -> float:
        return min(self.numbers)

def get_three_numbers() -> NumberSet:
    """
    Prompts the user to input exactly three numbers separated by spaces.
    Retries until valid input is received.
    """
    while True:
        try:
            inputs = input("Enter three numbers separated by space: ").split()
            if len(inputs) != 3:
                raise ValueError("Exactly three numbers are required.")
            nums = tuple(map(float, inputs))
            return NumberSet(nums)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main() -> None:
    number_set = get_three_numbers()
    print(f"Largest number: {number_set.largest()}")
    print(f"Smallest number: {number_set.smallest()}")

if __name__ == "__main__":
    main()
