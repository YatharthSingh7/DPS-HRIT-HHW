import math

def compute_gcd_lcm():
    while True:
        try:
            print("\n=== GCD & LCM Calculator ===")
            user_input = input("👉 Enter two non-zero integers separated by space (or type 'exit' to quit): ").strip()

            if user_input.lower() == 'exit':
                print("👋 Exiting. Thanks for using the calculator!")
                break

            parts = user_input.split()
            if len(parts) != 2:
                print("❌ Please enter exactly two numbers.\n")
                continue

            a, b = map(int, parts)

            if a == 0 or b == 0:
                print("❌ GCD/LCM is undefined for zero. Try again.\n")
                continue

            gcd_val = math.gcd(a, b)
            lcm_val = abs(a * b) // gcd_val

            print(f"✅ GCD({a}, {b}) = {gcd_val}")
            print(f"✅ LCM({a}, {b}) = {lcm_val}")

        except ValueError:
            print("❌ Invalid input. Please enter valid integers.\n")
        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")

# ✅ Call this directly to run
if __name__ == "__main__":
    compute_gcd_lcm()
