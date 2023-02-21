
# Classes

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        name_and_surname = f'\nName: {self.name}\nSurname: {self.surname}'
        average_score = '\nAverage score for homeworks: ' + '{0:.1f}'.format(self.get_average_HW_score())

        current = ", ".join(self.finished_courses)
        in_progress = 'none' if not current else current
        in_progress_str = f'\nCourses in progress: {", ".join(self.courses_in_progress)}'

        may_be_finish = ", ".join(self.finished_courses)
        finished = 'none' if not may_be_finish else may_be_finish
        finished_str = f'\nCourses finished: {finished}'

        return name_and_surname + average_score + in_progress_str + finished_str

    def get_average_HW_score(self):
        grade_values = self.grades.values()
        list_values = [item for sublist in grade_values for item in sublist]
        if not list_values:
            return 0
        else:
            return sum(list_values) / len(list_values)

    def rate_lecture(self, lecturer, course, grade):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            raise ValueError(f"Student {self.name} can't rate course {course} for {lecturer.name}")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f'\nName: {self.name}\nSurname: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __str__(self):
        super_str = Mentor.__str__(self)
        average_score = '\nAverage score for lectures: ' + '{0:.1f}'.format(self.get_average_score())
        return super_str + average_score 

    def get_average_score(self):
        grade_values = self.grades.values()
        list_values = [item for sublist in grade_values for item in sublist]
        if not list_values:
            return 0
        else:
            return sum(list_values) / len(list_values)

class Reviewer(Mentor):  
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise ValueError(f"Reviewer {self.name} can't rate course {course} of {student.name}")

# functions

def get_average_score_hw(students, course):
    if len(students):
        score = 0
        count = 0
        for student in students:
            if isinstance(student, Student) and course in student.grades:
                grades = student.grades[course]
                score += sum(grades)
                count += len(grades)
        if count:
            return score / count
        else:
            return 'no scores'
    else:
        return 'no students'

def get_average_score_lectures(lecturers, course):
    if len(lecturers):
        score = 0
        count = 0
        for lecturer in lecturers:
            if isinstance(lecturer, Lecturer) and course in lecturer.grades:
                grades = lecturer.grades[course]
                score += sum(grades)
                count += len(grades)
        if count:
            return score / count
        else:
            return 'no scores'
    else:
        return 'no lecturers'


# some mentors ans students

a_student = Student('Jon', 'Adams', 'male')
a_student.courses_in_progress += ['Python']
a_student.courses_in_progress += ['Swift']

b_student = Student('Kelly', 'Bohn', 'female')
b_student.courses_in_progress += ['Python']
b_student.courses_in_progress += ['Basic']

best_lecturer = Lecturer('Ron', 'Bohn')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Swift']

busy_lecturer = Lecturer('Ander', 'Buster')
busy_lecturer.courses_attached += ['Basic']
 
cool_reviewer = Reviewer('Pol', 'Hudson')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Swift']

lol_reviewer = Reviewer('James', 'Joker')
lol_reviewer.courses_attached += ['Basic'] 

# a sample run

a_student.rate_lecture(best_lecturer, 'Python', 10)
a_student.rate_lecture(best_lecturer, 'Swift', 9)
b_student.rate_lecture(best_lecturer, 'Python', 7)
b_student.rate_lecture(busy_lecturer, 'Basic', 6)

cool_reviewer.rate_hw(a_student, 'Python', 8)
cool_reviewer.rate_hw(a_student, 'Python', 7)
cool_reviewer.rate_hw(a_student, 'Python', 10)
cool_reviewer.rate_hw(a_student, 'Swift', 8)
cool_reviewer.rate_hw(b_student, 'Python', 9)
cool_reviewer.rate_hw(b_student, 'Python', 5)

lol_reviewer.rate_hw(b_student, 'Basic', 4)
lol_reviewer.rate_hw(b_student, 'Basic', 5)
lol_reviewer.rate_hw(b_student, 'Basic', 7)

# results

print('\n* Some programming school *')

print('\n* Students:')
print(a_student)
print(b_student)

print('\n* Lectures:')
print(best_lecturer)
print(busy_lecturer)

print('\n* Reviewers:')
print(cool_reviewer)
print(lol_reviewer)

courses = ['Basic', 'Python', 'Swift']
students = [a_student, b_student]
print('\n* Ratings:\n')
for course in courses:
    av_score_hw = get_average_score_hw(students, course)
    if type(av_score_hw) == float:
        av_score_hw = '{0:.1f}'.format(av_score_hw)
    print(f'Average score of homeworks for course {course}: ' + av_score_hw)

print()
lecturers = [best_lecturer, busy_lecturer]
for course in courses:
    av_score_lec = get_average_score_lectures(lecturers, course)
    if type(av_score_lec) == float:
        av_score_lec = '{0:.1f}'.format(av_score_lec)
    print(f'Average score of lectures for course {course}: ' + av_score_lec)

print()
