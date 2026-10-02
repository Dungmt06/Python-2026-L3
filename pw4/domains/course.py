class Course:
    def __init__(self, cid, name):
        self.id, self.name = cid, name

    def __str__(self):
        return f"[{self.id}] {self.name}"