students = {}

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added!\n")

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

def show_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")
    for name, marks in students.items():
        grade = get_grade(marks)
        print(f"{name}: {marks} marks | Grade {grade}")
    print()

while True:
    print("===== MENU =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
