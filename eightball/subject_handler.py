class SubjectHandler:
    def __init__(self):
        self.subjects = []

    def AddSubject(self,subject):
        self.subjects.append(subject)

    def draw_subjects(self):
        for subject in self.subjects:
            subject.draw()

    def move_subjects(self, dt):
        for subject in self.subjects:
            subject.move(dt)