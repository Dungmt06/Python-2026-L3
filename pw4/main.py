import curses
from input import input_students, input_courses, input_marks
from output import display_menu, show_students_sorted

def main(stdscr):
    students, courses, marks = [], [], {}

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
            break

if __name__ == "__main__":
    curses.wrapper(main)