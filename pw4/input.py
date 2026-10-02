from domains.student import Student
from domains.course import Course

def input_students(students):
    count = int(input("Enter number of students: "))
    for _ in range(count):
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        students.append(Student(sid, name, dob))

def input_courses(courses):
    count = int(input("Enter number of courses: "))
    for _ in range(count):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        courses.append(Course(cid, name))

def input_marks(students, courses, marks):
    if not courses or not students:
        print("Please enter student and course lists first!")
        return

    print("Available Courses")
    for course in courses:
        print(course)

    cid = input("Select Course ID: ")
    course_exists = any(c.get_id() == cid for c in courses)
    if not course_exists:
        print("Course not found!")
        return

    print(f"Entering marks for Course ID: {cid}")
    for student in students:
        sid = student.get_id()
        name = student.get_name()
        mark = float(input(f"Mark for {name} ({sid}): "))
        marks[(cid, sid)] = mark