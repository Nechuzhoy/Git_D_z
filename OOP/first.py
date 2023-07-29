class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def averages(self):
        return sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.averages()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {"".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        return self.averages() < other.averages()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        self.lec_grades = {}

    def average(self):
        return sum([sum(grade) for grade in self.lec_grades.values()]) / sum(
            [len(grade) for grade in self.lec_grades.values()])

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.average()}'
        return res

    def __lt__(self, other):
        return self.average() < other.average()


class Reviewer(Mentor):
    def rate_rev(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student1 = Student('Дуська', 'Педалькина', 'Герл')
student2 = Student('Васька', 'Донный', 'Бой')

reviewer1 = Reviewer('Эдик', 'Выживший')
reviewer2 = Reviewer('Гарик', 'Невесомый')

lecturer1 = Lecturer('Юра', 'Бывалый')
lecturer2 = Lecturer('Аладин', 'Сидоров')

student1.courses_in_progress += ['Как выжить за МКАД']
student1.courses_in_progress += ['Как дышать в невесомости']
student2.courses_in_progress += ['Как выжить за МКАД']
student2.courses_in_progress += ['Как дышать в невесомости']

reviewer1.courses_attached += ['Как выжить за МКАД']
reviewer2.courses_attached += ['Как дышать в невесомости']

reviewer1.rate_rev(student1, 'Как выжить за МКАД', 2)
reviewer1.rate_rev(student1, 'Как выжить за МКАД', 2)
reviewer1.rate_rev(student1, 'Как выжить за МКАД', 2)
reviewer2.rate_rev(student1, 'Как дышать в невесомости', 1)
reviewer2.rate_rev(student1, 'Как дышать в невесомости', 1)
reviewer2.rate_rev(student1, 'Как дышать в невесомости', 1)

reviewer1.rate_rev(student2, 'Как выжить за МКАД', 5)
reviewer1.rate_rev(student2, 'Как выжить за МКАД', 5)
reviewer1.rate_rev(student2, 'Как выжить за МКАД', 5)
reviewer2.rate_rev(student2, 'Как дышать в невесомости', 3)
reviewer2.rate_rev(student2, 'Как дышать в невесомости', 3)
reviewer2.rate_rev(student2, 'Как дышать в невесомости', 3)

student1.finished_courses += ['Поднять солнце вручную']
student2.finished_courses += ['Вызов джина']

lecturer1.courses_attached += ['Поднять солнце вручную']
lecturer1.courses_attached += ['Вызов джина']
lecturer2.courses_attached += ['Вызов джина']
lecturer2.courses_attached += ['Поднять солнце вручную']

student1.rate_lec(lecturer1, 'Поднять солнце вручную', 10)
student1.rate_lec(lecturer1, 'Поднять солнце вручную', 10)
student1.rate_lec(lecturer1, 'Поднять солнце вручную', 10)
student2.rate_lec(lecturer1, 'Вызов джина', 8)
student2.rate_lec(lecturer1, 'Вызов джина', 8)
student2.rate_lec(lecturer1, 'Вызов джина', 8)

student2.rate_lec(lecturer2, 'Вызов джина', 9)
student2.rate_lec(lecturer2, 'Вызов джина', 9)
student2.rate_lec(lecturer2, 'Вызов джина', 9)
student1.rate_lec(lecturer2, 'Поднять солнце вручную', 5)
student1.rate_lec(lecturer2, 'Поднять солнце вручную', 5)
student1.rate_lec(lecturer2, 'Поднять солнце вручную', 5)


def average_g_s(list_st, course):
    return sum([sum(i.grades[course]) for i in list_st]) / sum([len(i.grades[course]) for i in list_st])


def average_g_l(list_lec, course):
    return sum([sum(i.lec_grades[course]) for i in list_lec]) / sum([len(i.lec_grades[course]) for i in list_lec])


print(lecturer2.lec_grades)
print('--------------------')
print('У проверяющих:')
print(reviewer1)
print('--------------------')
print('У лекторов:')
print('--------------------')
print(lecturer2)
print('--------------------')
print('У студентов:')
print('--------------------')
print(student1)
print('--------------------')
print("Оценки студентам")
print('--------------------')
print(student1.grades)
print(student2.grades)
print('--------------------')
print("Оценки лекторам")
print('--------------------')
print(lecturer1.lec_grades)
print(lecturer2.lec_grades)
print('--------------------')
print('У проверяющих:')
print('--------------------')
print(reviewer1)
print('--------------------')
print(reviewer2)
print('--------------------')
print('У лекторов:')
print('--------------------')
print(lecturer1)
print('--------------------')
print(lecturer2)
print(lecturer1 < lecturer2)
print('--------------------')
print('У студентов:')
print('--------------------')
print(student1)
print('--------------------')
print(student2)
print(student1 > student2)
print('--------------------')
print(average_g_s([student1, student2], 'Как дышать в невесомости'))
print('--------------------')
print(average_g_l([lecturer1, lecturer2], 'Поднять солнце вручную'))
