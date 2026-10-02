import input as in_mod
import output as out_mod

def main():
    students = []
    courses = []
    marks = {}

    while True:
        print("STUDENT MARK MANAGEMENT SYSTEM")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks for Course")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks for Course")
        print("0. Exit")
        
        choice = input("Select option (0-6): ")
        if choice == '1':
            in_mod.input_students(students)
        elif choice == '2':
            in_mod.input_courses(courses)
        elif choice == '3':
            in_mod.input_marks(students, courses, marks)
        elif choice == '4':
            out_mod.list_students(students)
        elif choice == '5':
            out_mod.list_courses(courses)
        elif choice == '6':
            out_mod.show_student_marks(students, marks)
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()