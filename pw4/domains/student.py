import math
import numpy as np

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