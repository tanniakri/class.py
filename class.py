class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Mentor) and course in self.finished_courses and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _grad_(self, grad):
        grad = (sum((self.grades).get('Python'))) / (len((self.grades).get('Python')))
        return grad
    
    def __lt__(self, other):
        return self.grad < other.grad
                 
    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка за домашнее задание: {self._grad_} Курсы в процессе изучения: {', '.join(self.courses_in_progress)} Завершенные курсы: {', '.join(self.finished_courses)}'     
    
      

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _grad_(self, grad):
        grad = (sum((self.grades).get('Python'))) / (len((self.grades).get('Python')))
        return grad  
    
    def __lt__(self, other):
        return self.grad < other.grad 
     
    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка лекций: {self._grad_}' 



class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname}'    



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

coolll_mentor = Lecturer('Some', 'Buddy')
# coolll_mentor.courses_attached += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)



#best_student.__init__(coolll_mentor, 'Python', 10) 




# print(best_student.grades)
# print(coolll_mentor.grades)
print(cool_mentor)
print(best_student)
print(coolll_mentor)