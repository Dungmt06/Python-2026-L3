import curses
import os
import zipfile
from domains.student import Student
from domains.course import Course
from input import input_students, input_courses, input_marks
from output import display_menu, show_students_sorted

DATA_ARCHIVE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def load_data(students, courses, marks):
    if os.path.exists(DATA_ARCHIVE):
        with zipfile.ZipFile(DATA_ARCHIVE, 'r') as zip_ref:
            zip_ref.extractall()

    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                if line.strip():
                    sid, name, dob = line.strip().split(",")
                    students.append(Student(sid, name, dob))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                if line.strip():
                    cid, name, credits = line.strip().split(",")
                    courses.append(Course(cid, name, credits))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                if line.strip():
                    cid, sid, score = line.strip().split(",")
                    marks[(cid, sid)] = float(score)

    for s in students:
        s.calc_gpa(marks, courses)

def compress_data():
    with zipfile.ZipFile(DATA_ARCHIVE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in TXT_FILES:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)

def main(stdscr):
    students, courses, marks = [], [], {}
    load_data(students, courses, marks)

    while True:
        display_menu(stdscr)
        c = stdscr.getkey()

        if c == '1':
            input_students(stdscr, students)
            stdscr.addstr("\nPress any key to return ")
            stdscr.refresh()
            stdscr.getch()
        elif c == '2':
            input_courses(stdscr, courses)
            stdscr.addstr("\nPress any key to return ")
            stdscr.refresh()
            stdscr.getch()
        elif c == '3':
            input_marks(stdscr, students, courses, marks)
            stdscr.addstr("\nPress any key to return ")
            stdscr.refresh()
            stdscr.getch()
        elif c == '4':
            show_students_sorted(stdscr, students)
        elif c == '0':
            compress_data()
            break

if __name__ == "__main__":
    curses.wrapper(main)