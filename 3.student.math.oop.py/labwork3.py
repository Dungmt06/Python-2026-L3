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
        m, cr = [], []
        for c in courses:
            if (c.id, self.id) in marks:
                m.append(marks[(c.id, self.id)])
                cr.append(c.credits)
        if cr:
            g = np.sum(np.array(m) * np.array(cr)) / np.sum(cr)
            self.gpa = math.floor(g * 10) / 10
        else:
            self.gpa = 0.0

    def __str__(self):
        return f"[{self.id}] {self.name} - DoB: {self.dob} - GPA: {self.gpa}"

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
        stdscr.clear()
        stdscr.addstr(0, 0, prompt)
        stdscr.refresh()
        curses.echo()
        text = stdscr.getstr(1, 0).decode('utf-8')
        curses.noecho()
        return text

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "STUDENT MANAGEMENT ")
        stdscr.addstr(1, 0, "1. Input Students\n2. Input Courses\n3. Input Marks\n4. Show Students (GPA)\n0. Exit")
        stdscr.addstr(7, 0, "Select: ")
        stdscr.refresh()

        c = stdscr.getkey()

        if c == '1':
            n = int(get_input("Number of students: "))
            for _ in range(n):
                students.append(Student(get_input("ID: "), get_input("Name: "), get_input("DoB: ")))

        elif c == '2':
            n = int(get_input("Number of courses: "))
            for _ in range(n):
                courses.append(Course(get_input("ID: "), get_input("Name: "), get_input("Credits: ")))

        elif c == '3':
            cid = get_input("Course ID: ")
            for s in students:
                m = float(get_input(f"Mark for {s.name}: "))
                marks[(cid, s.id)] = math.floor(m * 10) / 10
                s.calc_gpa(marks, courses)

        elif c == '4':
            students.sort(key=lambda s: s.gpa, reverse=True)
            stdscr.clear()
            stdscr.addstr(0, 0, "STUDENT LIST (Sorted by GPA) ")
            for i, s in enumerate(students):
                stdscr.addstr(i + 2, 0, str(s))
            stdscr.addstr(len(students) + 3, 0, "Press any key to return ")
            stdscr.refresh()
            stdscr.getch()

        elif c == '0':
            break

if __name__ == "__main__":
    curses.wrapper(main)