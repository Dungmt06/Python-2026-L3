import math
import numpy as np
import curses

class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        self.gpa = 0.0

    def calc_gpa(self, marks, courses):
        m = [marks[(c.id, self.id)] for c in courses if (c.id, self.id) in marks]
        cr = [c.credits for c in courses if (c.id, self.id) in marks]
        
        if cr:
            g = np.sum(np.array(m) * np.array(cr)) / np.sum(cr)
            self.gpa = math.floor(g * 10) / 10.0
        else:
            self.gpa = 0.0

    def __str__(self):
        return f"[{self.id}] {self.name} - DoB: {self.dob} - GPA: {self.gpa:.1f}"

class Course:
    def __init__(self, cid, name, credits):
        self.id = cid
        self.name = name
        self.credits = float(credits)

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.credits} cr)"

def main(stdscr):
    students, courses, marks = [], [], {}

    def get_input(prompt):
        stdscr.addstr(prompt)
        stdscr.refresh()
        curses.echo()
        curses.curs_set(1)
        y, x = stdscr.getyx()
        val = stdscr.getstr(y, x).decode('utf-8').strip()
        curses.noecho()
        curses.curs_set(0)
        stdscr.addstr("\n")
        return val

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Student management system\n1. Input students\n2. Input courses\n3. Input marks\n4. Show students (Sorted by GPA)\n0. Exit\n\nSelect option: ")
        stdscr.refresh()
        
        c = stdscr.getkey()

        if c == '1':
            stdscr.clear()
            n = int(get_input("Number of students: "))
            for i in range(n):
                stdscr.addstr(f"\nStudent {i+1}:\n")
                sid = get_input("ID: ")
                name = get_input("Name: ")
                dob = get_input("DoB: ")
                students.append(Student(sid, name, dob))
            
            stdscr.addstr("\nPress any key to return ")
            stdscr.refresh()
            stdscr.getch()

        elif c == '2':
            stdscr.clear()
            n = int(get_input("Number of courses: "))
            for i in range(n):
                stdscr.addstr(f"\nCourse {i+1}:\n")
                cid = get_input("ID: ")
                cname = get_input("Name: ")
                credits = get_input("Credits: ")
                courses.append(Course(cid, cname, credits))

            stdscr.addstr("\nPress any key to return ")
            stdscr.refresh()
            stdscr.getch()

        elif c == '3':
            stdscr.clear()
            if not courses or not students:
                stdscr.addstr(0, 0, "Add students and courses: \nPress any key to return ")
                stdscr.refresh()
                stdscr.getch()
                continue

            cid = get_input("Course ID: ")
            stdscr.addstr(f"Inputting marks for course {cid}:\n")
            for s in students:
                m = float(get_input(f"Mark for {s.name} ({s.id}): "))
                marks[(cid, s.id)] = math.floor(m * 10) / 10.0
                s.calc_gpa(marks, courses)

            stdscr.addstr("\nPress any key to return ")
            stdscr.refresh()
            stdscr.getch()

        elif c == '4':
            stdscr.clear()
            if students:
                gpas = np.array([s.gpa for s in students])
                sorted_indices = np.argsort(-gpas)
                sorted_students = [students[i] for i in sorted_indices]
                
                stdscr.addstr(0, 0, "Students list (Sorted by GPA)\n")
                for s in sorted_students:
                    stdscr.addstr(str(s) + "\n")
            else:
                stdscr.addstr(0, 0, "Error: No students found ")
                
            stdscr.addstr("Press any key to return ")
            stdscr.refresh()
            stdscr.getch()
        elif c == '0':
            break

if __name__ == "__main__":
    curses.wrapper(main)