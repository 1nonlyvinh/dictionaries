def main():
    grades = {"Maya": 100, "JP": 99, "Erica": 98, "Vincent": 80}
    fetch_grades(grades)

def fetch_grades(student_grades): 
    for grade in student_grades: 
        print(f"{grade} has a grade of a {student_grades[grade]}")
main() 