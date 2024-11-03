class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def total_marks(self):
        return sum(self.marks.values())

    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return self.total_marks() / len(self.marks)


if __name__ == '__main__':
    student = Student(input("Enter student name: "))

    while True:
        subject = input("Enter name of subject: ")
        mark = int(input("Enter mark: "))
        student.add_mark(subject, mark)