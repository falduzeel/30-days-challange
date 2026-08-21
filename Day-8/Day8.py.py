def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

students_data = {
    "Zeel": 88,
    "Aarav": 94,
    "Rohan": 65,
    "Priya": 42
}

print("=== Day 8: Student Grade Calculator ===")

for student, score in students_data.items():
    grade = calculate_grade(score)
    print(f"Student: {student} | Marks: {score} | Grade: {grade}")