import numpy as np

def display_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Student management system\n1. Input students\n2. Input courses\n3. Input marks\n4. Show students (Sorted by GPA)\n0. Exit\n\nSelect option: ")
    stdscr.refresh()

def show_students_sorted(stdscr, students):
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
        
    stdscr.addstr("\nPress any key to return ")
    stdscr.refresh()
    stdscr.getch()