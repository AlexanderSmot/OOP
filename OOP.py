class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def st_avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей не сравниваем.")
            return
        return self.st_avg_rate() < other.st_avg_rate()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей не сравниваем.")
            return
        return self.st_avg_rate() > other.st_avg_rate()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей не сравниваем.")
            return
        return self.st_avg_rate() == other.st_avg_rate()

    def __str__(self):
        return f' Имя: {self.name} \n ' \
               f'Фамилия: {self.surname} \n ' \
               f'Средняя оценка за домашние задания: {self.st_avg_rate()} \n ' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n ' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def __str__(self):
        return f' Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.avg_rate()}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей не сравниваем.")
            return
        return self.st_avg_rate() < other.st_avg_rate()

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f' Имя: {self.name} \n Фамилия: {self.surname}'


best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_1.finished_courses += ['Введение в программирование']

best_student_2 = Student('Maks', 'Min', 'your_gender')
best_student_2.courses_in_progress += ['C++', 'Git']
best_student_2.finished_courses += ['Введение в программирование']

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Who', 'Nobody')
cool_reviewer_2.courses_attached += ['Python']

cool_reviewer_1.rate_hw(best_student_1, 'Python', 7)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)

cool_reviewer_2.rate_hw(best_student_2, 'Python', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 7)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 6)


some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)

cool_lecturer_1 = Lecturer('Some', 'Buddy')
cool_lecturer_1.courses_attached += ['Python', 'C+']
cool_lecturer_2 = Lecturer('Mr', 'Voice')
cool_lecturer_2.courses_attached += ['Git', 'C+']


best_student_1.lecturer_grade(cool_lecturer_1, 'Python', 8)
best_student_1.lecturer_grade(cool_lecturer_1, 'Python', 7)
best_student_1.lecturer_grade(cool_lecturer_1, 'Python', 10)

print(best_student_1.grades)
print(cool_lecturer_1.grades)
print(cool_lecturer_1)
print(best_student_1)

if best_student_1 < best_student_2:
    print(best_student_1.name, ' has less rate than', best_student_2.name)
elif best_student_1 > best_student_2:
    print(best_student_1.name, ' has higher rate than', best_student_2.name)
else:
    print(best_student_1.name, ' has the same rate as', best_student_2.name)
