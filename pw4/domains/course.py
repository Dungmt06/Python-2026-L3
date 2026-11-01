class Course:
    def __init__(self, cid, name, credits):
        self.id = cid
        self.name = name
        self.credits = float(credits)

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.credits} cr)"