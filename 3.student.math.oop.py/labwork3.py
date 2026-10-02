class Student:
    def __init__(self, sid, name, dob):
        self.id, self.name, self.dob = sid, name, dob
    def __str__(self):
        return f"[{self.id}] {self.name} - {self.dob}"

class Course:
    def __init__(self, cid, name):
        self.id, self.name = cid, name
    def __str__(self):
        return f"[{self.id}] {self.name}"

class StudentMarkManagement:
    def __init__(self):
        self.students, self.courses, self.marks = [], [], {}

    def input_students(self):
        for _ in range(int(input("Number of students: "))):
            self.students.append(Student(input("ID: "), input("Name: "), input("DoB: ")))

    def input_courses(self):
        for _ in range(int(input("Number of courses: "))):
            self.courses.append(Course(input("Course ID: "), input("Course Name: ")))

    def input_marks(self):
        self.list_courses()
        cid = input("Select Course ID: ")
        for s in self.students:
            self.marks[(cid, s.id)] = float(input(f"Mark for {s.name} ({s.id}): "))

    def list_students(self):
        print("Students:")
        for s in self.students: print(s)

    def list_courses(self):
        print("Courses:")
        for c in self.courses: print(c)

    def show_marks(self):
        cid = input("Enter Course ID to view marks: ")
        print(f"Marks for {cid}:")
        for s in self.students:
            print(f"{s.name} ({s.id}): {self.marks.get((cid, s.id), 'N/A')}")

if __name__ == "__main__":
    m = StudentMarkManagement()
    m.input_students()
    m.input_courses()
    m.input_marks()
    m.list_students()
    m.list_courses()
    m.show_marks()