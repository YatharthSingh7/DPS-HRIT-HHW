import platform
from datetime import datetime
import random

def get_custom_welcome() -> str:
    """
    Returns a custom welcome message written with a professional tone.
    """
    return (
        "Welcome to your Python programming session!\n"
        "Harness the power of clean code and thoughtful design to build scalable, maintainable solutions.\n"
    )

def get_inspirational_quote() -> str:
    """
    Returns a random inspirational programming quote.
    """
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad. — Cory House",
        "Programs must be written for people to read, and only incidentally for machines to execute. — Harold Abelson",
        "Experience is the name everyone gives to their mistakes. — Oscar Wilde",
        "Simplicity is the soul of efficiency. — Austin Freeman",
        "Before software can be reusable it first has to be usable. — Ralph Johnson",
        "Clean code always looks like it was written by someone who cares. — Michael Feathers",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. — Martin Fowler",
    ]
    return random.choice(quotes)

def display_welcome() -> None:
    """
    Displays a welcome message with system info, timestamp, custom message, and an inspirational quote.
    """
    info = platform.uname()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"=== Welcome ===")
    print(f"Timestamp: {timestamp}")
    print(f"System: {info.system} ({info.machine})")
    print(f"Processor: {info.processor}\n")
    print(get_custom_welcome())
    print(f"\nQuote of the session:\n\"{get_inspirational_quote()}\"")
    print("=" * 50)

if __name__ == "__main__":
    display_welcome()
