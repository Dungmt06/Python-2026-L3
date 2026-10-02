class Student:
    def __init__(self, sid, name, dob):
        self.id, self.name, self.dob = sid, name, dob

    def __str__(self):
        return f"[{self.id}] {self.name} - {self.dob}"