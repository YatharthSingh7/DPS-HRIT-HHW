def search_element():
    while True:
        try:
            print("\n=== 🔍 Search Element in List/Tuple ===")
            user_input = input("👉 Enter list elements separated by space (or type 'exit' to quit): ").strip()

            if user_input.lower() == 'exit':
                print("👋 Exiting.")
                break

            if not user_input:
                print("❌ Input cannot be empty. Please try again.\n")
                continue

            elements = user_input.split()

            if len(elements) == 0:
                print("❌ No elements entered. Try again.\n")
                continue

            search_for = input("🔎 Enter the element you want to search for: ").strip()

            if not search_for:
                print("❌ You must enter something to search for.\n")
                continue

            if search_for in elements:
                index = elements.index(search_for)
                print(f"✅ '{search_for}' found at position {index} (0-based index).\n")
            else:
                print(f"❌ '{search_for}' not found in the list.\n")

        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")

# Run the function directly
if __name__ == "__main__":
    search_element()
