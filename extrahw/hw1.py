# ============================================================
#  PROJECT 1: Student Grade Manager
#  Use a list of dictionaries to store student records.
#  Each student has a name and a list of grades.
# ============================================================


class GradeManager:

    def __init__(self):
        self.students = []

    def add_student(self, name):
        if any(s["name"].lower() == name.lower() for s in self.students):
            print(f"Student '{name}' already exists.")
            return

        self.students.append({"name": name, "grades": []})
        print(f"Added student '{name}'.")

    def add_grade(self, name, grade):
        for student in self.students:
            if student["name"].lower() == name.lower():
                if 0 <= grade <= 100:
                    student["grades"].append(grade)
                    print(f"Added grade {grade} for '{student['name']}'.")
                else:
                    print(f"Error: grade {grade} is out of range (0-100).")
                return
        print(f"Student '{name}' not found.")

    def get_average(self, name):
        for student in self.students:
            if student["name"].lower() == name.lower():
                grades = student["grades"]
                if not grades:
                    print(f"'{student['name']}' has no grades yet.")
                    return None
                avg = sum(grades) / len(grades)
                print(f"'{student['name']}' average: {avg:.2f}")
                return avg
        print(f"Student '{name}' not found.")
        return None

    def top_students(self, n=3):
        ranked = [s for s in self.students if s["grades"]]
        ranked = sorted(
            ranked,
            key=lambda s: sum(s["grades"]) / len(s["grades"]),
            reverse=True,
        )

        print(f"\nTop {n} Students:")
        for i, student in enumerate(ranked[:n], start=1):
            avg = sum(student["grades"]) / len(student["grades"])
            print(f"{i}. {student['name']} — {avg:.2f}")

    def class_summary(self):
        all_grades = [g for s in self.students for g in s["grades"]]

        if not all_grades:
            print("No grades recorded yet.")
            return

        print("\nClass Summary")
        print(f"Total students: {len(self.students)}")
        print(f"Highest grade: {max(all_grades)}")
        print(f"Lowest grade: {min(all_grades)}")
        print(f"Class average: {sum(all_grades) / len(all_grades):.2f}")

    def display_all(self):
        if not self.students:
            print("No students to show.")
            return

        print("\nAll Students")
        for student in self.students:
            print(f"{student['name']}: {student['grades']}")


# ── Main: Test your code here ─────────────────────────────
if __name__ == "__main__":

    manager = GradeManager()

    manager.add_student("Alice")
    manager.add_student("Bob")
    manager.add_student("Charlie")

    manager.add_grade("Alice", 92)
    manager.add_grade("Alice", 85)
    manager.add_grade("Alice", 78)

    manager.add_grade("Bob", 60)
    manager.add_grade("Bob", 70)

    manager.add_grade("Charlie", 95)
    manager.add_grade("Charlie", 99)
    manager.add_grade("Charlie", 91)

    manager.display_all()

    manager.get_average("Alice")

    manager.top_students()

    manager.class_summary()