# Problem Challenge: Student Gradebook System

# Write a Python program that simulates a simple gradebook for a university department.

# Requirements:

# Accept student records (name, matric number, and a list of courses with scores). 
# Example:

# {
#     "name": "Aisha Musa",
#     "matric": "STA/2021/011",
#     "courses": {
#         "MTH101": 65,
#         "STA103": 80,
#         "CSC105": 72
#     }
# }
 
# Support these features:

# Add a new student.
# Update a student’s score in a course.
# Compute GPA for a student (assume: A=5, B=4, C=3, D=2, F=0; GPA = weighted average).
# List the top 3 students by GPA.
# Save all student data to a JSON file and load it back when the program restarts.


import json


student = {
    "name": str(input("What's your name?")),
    "matric": input("What's your matric number?"),
    "courses": {
         "MTH101": int(input("Enter your MTH101 score:")),
        "STA103": int(input("Enter your STA103 score:")),
         "CSC105": int(input("Enter your CSC105 score:"))
    }
    
};
print(student);

features = input("What do you want to do? Add a new student, Update a student's score, Compute GPA, List top 3 students by GPA, Save data to JSON file, Load data from JSON file?")

def add_student(student):
    students.append(student)
    print("Student added successfully.")

def update_student_score(matric, course, new_score):
    for student in students:
        if student["matric"] == matric:
            student["courses"][course] = new_score
            print("Student score updated successfully.")
            return
    print("Student not found.")

def compute_gpa(matric):
    for student in students:
        if student["matric"] == matric:
            total_points = 0
            total_courses = 0
            for course, score in student["courses"].items():
                if score >= 70:
                    total_points += 5
                elif score >= 60:
                    total_points += 4
                elif score >= 50:
                    total_points += 3
                elif score >= 40:
                    total_points += 2
                else:
                    total_points += 0
                total_courses += 1
            gpa = total_points / total_courses if total_courses > 0 else 0
            print(f"GPA for {student['name']} is {gpa:.2f}")
            return
    print("Student not found.")

def list_top_students():
    if not students:
        print("No students available.")
        return
    # Compute GPA for all students
    for student in students:
        compute_gpa(student["matric"])
    # Sort students by GPA
    top_students = sorted(students, key=lambda x: x["gpa"], reverse=True)[:3]
    print("Top 3 students by GPA:")
    for student in top_students:
        print(f"{student['name']} - {student['gpa']:.2f}")

def save_data_to_json():
    with open("students.json", "w") as f:
        json.dump(students, f)
    print("Data saved to students.json")

def load_data_from_json():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
        print("Data loaded from students.json")
    except FileNotFoundError:
        print("No data file found.")




if features == "Add a new student":
    add_student(student)
    # Code to add a new student
    
    pass
elif features == "Update a student's score":
    matric = input("Enter the student's matric number: ")
    course = input("Enter the course code: ")
    new_score = int(input("Enter the new score: "))
    update_student_score(matric, course, new_score)
    # Code to update a student's score
    pass
elif features == "Compute GPA":
    matric = input("Enter the student's matric number: ")
    compute_gpa(matric)
    
    # Code to compute GPA
    pass
elif features == "List top 3 students by GPA":
    list_top_students()
    # Code to list top 3 students by GPA
    pass
elif features == "Save data to JSON file":
    save_data_to_json()
    # Code to save data to JSON file
    pass
elif features == "Load data from JSON file":
    load_data_from_json()   
    # Code to load data from JSON file
    pass




