def list_students(students):
    print("Students List")
    if not students:
        print("Student list is empty.")
        return
    for student in students:
        print(student)

def list_courses(courses):
    print("Courses List")
    if not courses:
        print("Course list is empty.")
        return
    for course in courses:
        print(course)

def show_student_marks(students, marks):
    cid = input("Enter Course ID to view marks: ")
    print(f"Marks for {cid} ")
    found = False
    for student in students:
        sid = student.get_id()
        name = student.get_name()
        mark = marks.get((cid, sid), 'N/A')
        if (cid, sid) in marks:
            found = True
        print(f"{name} ({sid}): {mark}")
        
    if not found:
        print("No marks recorded for this course yet.")