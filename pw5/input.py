import curses
import math
from domains.student import Student
from domains.course import Course

def get_input(stdscr, prompt):
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

def input_students(stdscr, students):
    stdscr.clear()
    n = int(get_input(stdscr, "Number of students: "))
    for i in range(n):
        stdscr.addstr(f"\nStudent {i+1}:\n")
        sid = get_input(stdscr, "ID: ")
        name = get_input(stdscr, "Name: ")
        dob = get_input(stdscr, "DoB: ")
        students.append(Student(sid, name, dob))

    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")

def input_courses(stdscr, courses):
    stdscr.clear()
    n = int(get_input(stdscr, "Number of courses: "))
    for i in range(n):
        stdscr.addstr(f"\nCourse {i+1}:\n")
        cid = get_input(stdscr, "ID: ")
        cname = get_input(stdscr, "Name: ")
        credits = get_input(stdscr, "Credits: ")
        courses.append(Course(cid, cname, credits))

    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c.id},{c.name},{c.credits}\n")

def input_marks(stdscr, students, courses, marks):
    stdscr.clear()
    if not courses or not students:
        stdscr.addstr(0, 0, "Add students and courses first.\nPress any key to return ")
        stdscr.refresh()
        stdscr.getch()
        return

    cid = get_input(stdscr, "Course ID: ")
    stdscr.addstr(f"Inputting marks for course {cid}:\n")
    for s in students:
        m = float(get_input(stdscr, f"Mark for {s.name} ({s.id}): "))
        score = math.floor(m * 10) / 10.0
        marks[(cid, s.id)] = score
        s.calc_gpa(marks, courses)

    with open("marks.txt", "w") as f:
        for (course_id, student_id), score in marks.items():
            f.write(f"{course_id},{student_id},{score}\n")