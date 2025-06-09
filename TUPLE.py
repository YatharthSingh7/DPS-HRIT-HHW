def find_largest_smallest():
    while True:
        try:
            print("\n=== 🔍 Largest & Smallest Finder ===")
            user_input = input("👉 Enter numbers separated by space (or type 'exit' to quit): ")

            if user_input.lower().strip() == 'exit':
                print("👋 Exiting.")
                break

            if not user_input.strip():
                print("❌ No input provided. Please try again.\n")
                continue

            # Split input and attempt to convert each item to float
            items = user_input.strip().split()
            numbers = []

            for item in items:
                try:
                    num = float(item)
                    numbers.append(num)
                except ValueError:
                    print(f"⚠️ Skipping invalid entry: '{item}' (not a number)")

            if not numbers:
                print("❌ No valid numbers entered. Please try again.\n")
                continue

            print(f"✅ Largest Number : {max(numbers)}")
            print(f"✅ Smallest Number: {min(numbers)}\n")

        except Exception as e:
            print(f"❌ Unexpected Error: {e}\n")

# Run it directly
if __name__ == "__main__":
    find_largest_smallest()
