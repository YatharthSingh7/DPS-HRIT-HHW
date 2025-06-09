def swap_even_odd():
    while True:
        try:
            print("\n=== 🔁 Swap Even-Odd Index Elements ===")
            user_input = input("👉 Enter elements separated by space (or type 'exit' to quit): ").strip()

            if user_input.lower() == 'exit':
                print("👋 Exiting.")
                break

            if not user_input:
                print("❌ Input cannot be empty. Please try again.\n")
                continue

            elements = user_input.split()

            if len(elements) < 2:
                print("⚠️ Enter at least 2 elements to perform swapping.\n")
                continue

            swapped = elements[:]  # Copy list to avoid in-place mutation

            for i in range(0, len(swapped) - 1, 2):
                swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]

            print(f"✅ Swapped List: {' '.join(swapped)}\n")

        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")

# Run the function directly
if __name__ == "__main__":
    swap_even_odd()
