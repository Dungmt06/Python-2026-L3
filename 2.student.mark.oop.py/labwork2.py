class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter student DoB: ")
    def list(self):
        print(f"[{self.__id}] {self.__name} - {self.__dob}")


class Course:
    def __init__(self, course_id="", name=""):
        self.__id = course_id
        self.__name = name
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course Name: ")
    def list(self):
        print(f"[{self.__id}] {self.__name}")


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
 
    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"Student {i+1}:")
            s = Student()
            s.input()
            self.__students.append(s)
 
    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for i in range(n):
            print(f"Course {i+1}:")
            c = Course()
            c.input()
            self.__courses.append(c)
 
    def input_marks(self):
        if not self.__courses or not self.__students:
            print("Add students and courses: ")
            return
        self.list_courses()
        cid = input("Select course ID to enter marks: ")

        if not any(c.get_id() == cid for c in self.__courses):
            print("Course ID not found")
            return
        print(f"Inputting marks for course {cid}:")
        for s in self.__students:
            mark = float(input(f"Mark for {s.get_name()} ({s.get_id()}): "))
            self.__marks[(cid, s.get_id())] = mark

    def list_students(self):
        print("Student List ")
        for s in self.__students:
            s.list()

    def list_courses(self):
        print("Course List ")
        for c in self.__courses:
            c.list()

    def show_student_marks(self):
        cid = input("Enter course ID to view marks: ")
        print(f"Marks for course {cid} ")
        for s in self.__students:
            sid = s.get_id()
            mark = self.__marks.get((cid, sid), "N/A")
            print(f"{s.get_name()} ({sid}): {mark}")


if __name__ == "__main__":
    app = StudentMarkManagement()
    app.input_students()
    app.input_courses()
    app.input_marks()
    app.list_students()
    app.list_courses()
    app.show_student_marks()