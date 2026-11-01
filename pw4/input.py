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

def input_courses(stdscr, courses):
    stdscr.clear()
    n = int(get_input(stdscr, "Number of courses: "))
    for i in range(n):
        stdscr.addstr(f"\nCourse {i+1}:\n")
        cid = get_input(stdscr, "ID: ")
        cname = get_input(stdscr, "Name: ")
        credits = get_input(stdscr, "Credits: ")
        courses.append(Course(cid, cname, credits))

def input_marks(stdscr, students, courses, marks):
    stdscr.clear()
    if not courses or not students:
        stdscr.addstr(0, 0, "Add students and courses \nPress any key to return ")
        stdscr.refresh()
        stdscr.getch()
        return

    cid = get_input(stdscr, "Course ID: ")
    stdscr.addstr(f"Inputting marks for course {cid}:\n")
    for s in students:
        m = float(get_input(stdscr, f"Mark for {s.name} ({s.id}): "))
        marks[(cid, s.id)] = math.floor(m * 10) / 10.0
        s.calc_gpa(marks, courses)