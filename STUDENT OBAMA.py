def get_example_students():
    return {
        '101': {'name': 'Aryan', 'marks': 72},
        '102': {'name': 'Priya', 'marks': 88},
        '103': {'name': 'Kabir', 'marks': 67},
        '104': {'name': 'Ishita', 'marks': 76},
        '105': {'name': 'Deleena', 'marks': 98}
    }

def students_above_75():
    try:
        print("=== 🎓 Student Marks Manager ===")

        use_examples = input("📦 Do you want to view example students? (yes/no): ").strip().lower()
        students = {}

        if use_examples == 'yes':
            students = get_example_students()
            print("\n📋 Example Students:")
            for roll, info in students.items():
                print(f"🔹 {info['name']} (Roll: {roll}) → Marks: {info['marks']}")

        add_custom = input("\n➕ Do you want to add your own students? (yes/no): ").strip().lower()

        if add_custom == 'yes':
            try:
                n = int(input("👥 How many students do you want to add? "))
                for i in range(n):
                    print(f"\n📄 Student {i+1}:")
                    roll = input("🆔 Enter roll number: ").strip()
                    if roll in students:
                        print("⚠️ Roll number already exists. Skipping.")
                        continue
                    name = input("📝 Enter name: ").strip()
                    marks = float(input("📊 Enter marks: "))
                    students[roll] = {'name': name, 'marks': marks}
            except ValueError:
                print("❌ Invalid number or marks entered. Skipping additional entries.")

        if not students:
            print("⚠️ No students to show.")
            return

        print("\n🏅 Students scoring above 75:")
        found = False
        for info in students.values():
            if info['marks'] > 75:
                print(f"✅ {info['name']} → Marks: {info['marks']}")
                found = True

        if not found:
            print("😐 No student scored above 75.")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run directly
if __name__ == "__main__":
    students_above_75()
