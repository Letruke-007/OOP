class Student:
    def __init__(self, name, surname, gender = 'None'):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Функция проставления оценки студентом лектору
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    # Функция вычисления средней оценки студента
    def __average(self):
        self.average = [grade for grades in self.grades.values() for grade in grades]
        if self.average:
            self.average_res = (sum(self.average)/len(self.average))
            return self.average_res
        else:
            return ("Пока нет оценок")

    # Функция сравнения средних баллов студентов
    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() == other.__average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() < other.__average()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() > other.__average()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
               f'{self.__average()}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:' \
               f' {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    # Функция вычисления средней оценки лектора
    def __average(self):
        self.average = [grade for grades in self.grades.values() for grade in grades]
        if self.average:
            self.average_res = (sum(self.average) / len(self.average))
            return self.average_res
        else:
            return ("Пока нет оценок")

    # Функция сравнения средних баллов лекторов
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() == other.__average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() < other.__average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() > other.__average()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average()}'

# Лекторы
lecturer_1 = Lecturer('Ivan', 'Gorin')
lecturer_1.courses_attached += 'Influence of an information in the modern world', 'JAVA Developer', 'Architecture', \
                               'Construction'

lecturer_2 = Lecturer('Andrey', 'Sergeev')
lecturer_2.courses_attached += 'Psychology', 'Relationships in the family'

# Студенты
student_1 = Student('John', 'Snow')
student_1.finished_courses += 'Modern technologies', 'Economy'
student_1.courses_in_progress += 'Influence of an information in the modern world', 'JAVA Developer'
student_1.rate_lecturer(lecturer_1, 'JAVA Developer', 9)
student_1.rate_lecturer(lecturer_2, 'Relationships in the family', 10)

student_2 = Student('Maria', 'Windzor', 'female')
student_2.finished_courses += 'Architecture', 'Construction'
student_2.courses_in_progress += 'Psychology', 'JAVA Developer'
student_2.rate_lecturer(lecturer_1, 'JAVA Developer', 8)
student_2.rate_lecturer(lecturer_2, 'Psychology', 10)

# Проверяющие
reviewer_1 = Reviewer('Alex', 'Morrison')
reviewer_1.courses_attached += 'Influence of an information in the modern world', 'JAVA Developer', 'Psychology'
reviewer_1.rate_hw(student_1, 'Influence of an information in the modern world', 7)
reviewer_1.rate_hw(student_1, 'JAVA Developer', 10)
reviewer_1.rate_hw(student_2, 'Psychology', 9)

reviewer_2 = Reviewer('Anna', 'Clark')
reviewer_1.courses_attached += 'Influence of an information in the modern world', 'JAVA Developer'
reviewer_2.rate_hw(student_1, 'Influence of an information in the modern world', 9)
reviewer_2.rate_hw(student_1, 'JAVA Developer', 7)

# Списки студентов и лекторов
Students = [student_1, student_2]
Lecturers = [lecturer_1, lecturer_2]

# Функция подсчета средней оценки по всем студентам в рамках конкретного курса
def average_grade_student_course(Students, course):
    average_grade = []
    for student in Students:
        if course in student.grades:
            average_grade += student.grades[course]
    if average_grade:
        return sum(average_grade) / len(average_grade)

# Функция подсчета средней оценки за лекции всех лекторов в рамках курса
def average_grade_lectors_course(Lecturers, course):
    average_grade = []
    for lecturer in Lecturers:
        if course in lecturer.grades:
            average_grade += lecturer.grades[course]
    if average_grade:
        return sum(average_grade) / len(average_grade)

print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()

