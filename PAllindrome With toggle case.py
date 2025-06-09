def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def toggle_case(s: str) -> str:
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s)

def run_palindrome_check():
    while True:
        try:
            print("\n=== Palindrome Checker & Case Toggler ===")
            s = input("👉 Enter a string (or type 'exit' to quit): ").strip()

            if s.lower() == "exit":
                print("👋 Exiting Palindrome Checker.")
                break

            if not s:
                print("❌ Empty input. Please enter a valid string.\n")
                continue

            result = is_palindrome(s)
            print(f"✅ Is Palindrome: {'Yes' if result else 'No'}")
            print(f"🔁 Toggled Case : {toggle_case(s)}\n")

        except Exception as e:
            print(f"❌ Unexpected Error: {e}\n")

# ✅ Call this to run directly
if __name__ == "__main__":
    run_palindrome_check()
