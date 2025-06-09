from functools import total_ordering
from typing import Tuple

@total_ordering
class Number:
    def __init__(self, value: float):
        self.value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Number):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Number):
            return NotImplemented
        return self.value < other.value

def get_two_numbers() -> Tuple[Number, Number]:
    """
    Prompt user to input exactly two numbers separated by space.
    Retry until valid input is received.
    """
    while True:
        try:
            inputs = input("Enter two numbers separated by space: ").split()
            if len(inputs) != 2:
                raise ValueError("Exactly two numbers required.")
            a, b = map(float, inputs)
            return Number(a), Number(b)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main() -> None:
    a, b = get_two_numbers()
    if a == b:
        print(f"Both numbers are equal: {a.value}")
    else:
        larger = max(a, b)
        smaller = min(a, b)
        print(f"Larger number: {larger.value}")
        print(f"Smaller number: {smaller.value}")

if __name__ == "__main__":
    main()
