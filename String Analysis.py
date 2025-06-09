from collections import Counter

def analyze_string():
    while True:
        try:
            print("\n=== String Analyzer ===")
            s = input("👉 Enter a string (or type 'exit' to quit): ").strip()

            if s.lower() == 'exit':
                print("👋 Exiting string analyzer.")
                break

            if not s:
                print("❌ Empty string. Please enter something meaningful.\n")
                continue

            stats = Counter({
                'vowels': 0, 'consonants': 0,
                'uppercase': 0, 'lowercase': 0,
                'digits': 0, 'special': 0
            })

            for ch in s:
                if ch.isalpha():
                    stats['vowels'] += ch.lower() in "aeiou"
                    stats['consonants'] += ch.lower() not in "aeiou"
                    stats['uppercase'] += ch.isupper()
                    stats['lowercase'] += ch.islower()
                elif ch.isdigit():
                    stats['digits'] += 1
                else:
                    stats['special'] += 1

            print("\n🧠 String Analysis Result:")
            for k, v in stats.items():
                print(f"{k.title():<12}: {v}")
            print()

        except Exception as e:
            print(f"❌ Error: {e}\n")

# ✅ Run directly
if __name__ == "__main__":
    analyze_string()


