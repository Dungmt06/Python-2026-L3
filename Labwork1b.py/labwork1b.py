# Practical Work 1: Student Mark Management

students = []  # format: [(id, name, dob), ...]
courses = []   # format: [(id, name), ...]
marks = {}     # format: {(course_id, student_id): mark}

# Input functions
def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_info():
    for _ in range(input_number_of_students()):
        students.append((input("ID: "), input("Name: "), input("DoB: ")))

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    for _ in range(input_number_of_courses()):
        courses.append((input("Course ID: "), input("Course Name: ")))

def input_marks():
    list_courses()
    cid = input("Select Course ID: ")
    for sid, name, _ in students:
        marks[(cid, sid)] = float(input(f"Mark for {name} ({sid}): "))

# Listing functions
def list_courses():
    print("Courses")
    for cid, name in courses:
        print(f"[{cid}] {name}")

def list_students():
    print("Students")
    for sid, name, dob in students:
        print(f"[{sid}] {name} - {dob}")

def show_student_marks():
    cid = input("\nEnter Course ID to view marks: ")
    print(f"Marks for {cid}")
    for sid, name, _ in students:
        print(f"{name} ({sid}): {marks.get((cid, sid), 'N/A')}")

# Execution
if __name__ == "__main__":
    input_student_info()
    input_course_info()
    input_marks()

    list_students()
    list_courses()
    show_student_marks()